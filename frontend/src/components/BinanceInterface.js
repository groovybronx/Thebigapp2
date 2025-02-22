import React, { useState, useEffect } from 'react';
import axios from '../services/api';

function BinanceInterface() {
  const [accountInfo, setAccountInfo] = useState(null);

  useEffect(() => {
    axios.get('/api/binance')
      .then(response => {
        setAccountInfo(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the account info!', error);
      });
  }, []);

  return (
    <div>
      <h1>Binance Account Information</h1>
      {accountInfo ? (
        <pre>{JSON.stringify(accountInfo, null, 2)}</pre>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

export default BinanceInterface;