import logo from "./logo.svg";
import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          <a href={`/login`} style={{ color: '#3182CE' }}>
            Login
          </a> or{' '}
          <a href={'/signup'} style={{ color: '#3182CE' }}>
            signup
          </a> to Assignmate
        </p>
      </header>
    </div>
  );
}

export default App;
