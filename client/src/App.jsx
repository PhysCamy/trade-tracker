import React from 'react';
import './App.css';
import Sidebar from './components/Sidebar';
import Home from './components/Home';
import Switch from '@mui/material/Switch';
import Portfolios from './components/Portfolios';

const App = () => {
  let component;

  switch (window.location.pathname) {
    case "/":
      component = <Home />;
      break;
    case "/portfolios":
      component = <Portfolios />;
      break;
    default:
      component = <Home />
  };

  return (
    <main className="grid grid-cols-[200px,_1fr]">
      <Sidebar />
      {component}
    </main>
  );
};

export default App;