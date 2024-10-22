import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Open your {' '}
          <a href={`/authenticate`} style={{ color: '#3182CE' }}>
            dashboard.
          </a>
        </p>
      </header>
    </div>
  );
}

export default App;
