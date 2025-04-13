import React, { useEffect, useState } from 'react';

function Leaderboard() {
  const [leaders, setLeaders] = useState([]);

  useEffect(() => {
    fetch('https://potential-halibut-9gw4ggqvxv5h99v-8000.app.github.dev/api/leaderboard')
      .then(response => response.json())
      .then(data => setLeaders(data));
  }, []);

  return (
    <div className="container mt-4">
      <h1 className="text-center mb-4">Leaderboard</h1>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Score</th>
          </tr>
        </thead>
        <tbody>
          {leaders.map(leader => (
            <tr key={leader.id}>
              <td>{leader.id}</td>
              <td>{leader.name}</td>
              <td>{leader.score}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Leaderboard;
