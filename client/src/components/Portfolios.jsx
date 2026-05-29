import React, { useEffect, useState} from 'react';
import api from '../api.js';
import AddPortfolioForm from './AddPortfolioForm.jsx';

const Portfolios = () => {
    const [portfolios, setPortfolios] = useState([]);

    const fetchPortfolios = async () => {
        try {
            const response = await api.get('/portfolios');
            setPortfolios(response.data)
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
    <div>
      <h2>Portfolios</h2>
      <ul>
        {portfolios.map((portfolio, index) => (
          <li key={index}>{portfolio.name}</li>
        ))}
      </ul>
      <AddPortfolioForm addPortfolio={addPortfolio} />
    </div>
  );
};

export default Portfolios;
