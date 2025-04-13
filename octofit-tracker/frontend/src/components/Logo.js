import React from 'react';
import logo from '../public/octofitapp-small.png';

function Logo() {
  return (
    <div style={{ display: 'flex', alignItems: 'center', padding: '10px' }}>
      <img src={logo} alt="Octofit Logo" style={{ height: '50px', marginRight: '10px' }} />
      <h1 style={{ color: '#4682b4', fontSize: '1.5rem' }}>Octofit Tracker</h1>
    </div>
  );
}

export default Logo;
