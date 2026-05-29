import React from 'react';
import './App.css';
import Sidebar from './components/Sidebar';
import Home from './components/Home';

const App = () => {
  return (
    <main className="grid gap-4 grid-cols-[200px,_1fr]">
      <Sidebar />
      <Home />
    </main>
  );
};

export default App;