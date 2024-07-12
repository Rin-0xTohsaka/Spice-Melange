import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import Chart from './components/Chart';

// Render the app normally
ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

// Expose the Chart component globally
window.EmbedableChart = {
  render: function(container) {
    ReactDOM.render(<Chart />, container);
  }
};