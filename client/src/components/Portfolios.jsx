import React, { useEffect, useState} from 'react';
import api from '../api.js';
import AddPortfolioForm from './AddPortfolioForm.jsx';
import { AllCommunityModule } from 'ag-grid-community';
import { AgGridProvider, AgGridReact } from 'ag-grid-react';
import { themeBalham } from 'ag-grid-community';

const Portfolios = () => {
    const [portfolios, setPortfolios] = useState([]);
    const [colDefs, setColDefs] = useState([
        { field: "id", headerName: "Portfolio ID", flex: 1 },
        { field: "name", headerName: "Name", flex: 1 },
        { field: "baseCcy", headerName: "Base Currency", flex: 1 }
    ]);
    const fetchPortfolios = async () => {
        try {
            const response = await api.get('/portfolios');
            setPortfolios(response.data.map((portfolio, index) => ({ id: portfolio.id, name: portfolio.name, baseCcy: portfolio.baseCcy ?? "ZZZ" })));
        } catch (error) {
            console.error("Error fetching portfolios.")
        }
    }
    const addPortfolio = async (id, name, baseCcy) => {
    try {
      await api.post('/portfolios/', { id: id, name: name, base_ccy: baseCcy });
      fetchPortfolios();
    } catch (error) {
      console.error("Error adding portfolio.", error);
    }
  };

  useEffect(() => {
    fetchPortfolios();
  }, []);

  return (
    <div className="bg-white pb-4 h-[200vh]">
      <AgGridProvider modules={[AllCommunityModule]}>
        <div style={{ height: 500 }}>
            <AgGridReact
                theme={themeBalham}
                rowData={portfolios}
                columnDefs={colDefs}
                domLayout='autoHeight'
            />
        </div>
      </AgGridProvider>
      <AddPortfolioForm addPortfolio={addPortfolio} />
    </div>
  );
};

export default Portfolios;
