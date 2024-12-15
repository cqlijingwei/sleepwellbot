import React, { useState } from 'react';
import ChatInterface from './components/ChatInterface';
import './app.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Sleep Better Support</h1>
      </header>
      <ChatInterface />
    </div>
  );
}

export default App;