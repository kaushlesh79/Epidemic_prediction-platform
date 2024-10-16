// Example: Simple Dashboard in React

import React, { useState, useEffect } from 'react';

const Dashboard = () => {
  const [epidemicData, setEpidemicData] = useState([]);

  useEffect(() => {
    fetch('/api/get-epidemic-data')
      .then(response => response.json())
      .then(data => setEpidemicData(data));
  }, []);

  return (
    <div>
      <h1>Epidemic Prediction Dashboard</h1>
      <table>
        <thead>
          <tr>
            <th>Region</th>
            <th>Disease</th>
            <th>Predicted Cases</th>
          </tr>
        </thead>
        <tbody>
          {epidemicData.map((item, index) => (
            <tr key={index}>
              <td>{item.region}</td>
              <td>{item.disease}</td>
              <td>{item.predicted_cases}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Dashboard;
