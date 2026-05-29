import React, { useState } from 'react';

const AddPortfolioForm = ({ addPortfolio }) => {
  const [portfolioId, setPortfolioId] = useState('');
  const [portfolioName, setPortfolioName] = useState('');
  const [portfolioBaseCcy, setPortfolioBaseCcy] = useState('');

  const handleAddPortfolio = (event) => {
    event.preventDefault();
    if (!!portfolioId && !!portfolioName && !!portfolioBaseCcy) {
      addPortfolio(portfolioId, portfolioName, portfolioBaseCcy);
      setPortfolioId('');
      setPortfolioName('');
      setPortfolioBaseCcy('')
    }
  };

  return (
    <form onClick={handleAddPortfolio}>
      <input
        type="text"
        value={portfolioId}
        onChange={(e) => setPortfolioId(e.target.value)}
        placeholder="ID"
      />
      <input
        type="text"
        value={portfolioName}
        onChange={(e) => setPortfolioName(e.target.value)}
        placeholder="Name"
      />
      <input
        type="text"
        value={portfolioBaseCcy}
        onChange={(e) => setPortfolioBaseCcy(e.target.value)}
        placeholder="Base Ccy"
      />
      <button type="submit">Add Portfolio</button>
    </form>
  );
};

export default AddPortfolioForm;