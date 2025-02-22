const express = require('express');
const mongoose = require('mongoose');
const Binance = require('node-binance-api');

const app = express();
const port = 5000;

// MongoDB connection
mongoose.connect('mongodb://mongodb:27017/binanceData', {  // Changed localhost to mongodb
  useNewUrlParser: true,
  useUnifiedTopology: true,
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Binance data schema
const binanceDataSchema = new mongoose.Schema({
  symbol: String,
  price: Number,
  timestamp: Date,
});

const BinanceData = mongoose.model('BinanceData', binanceDataSchema);

// Binance API setup
const binance = new Binance().options({
  APIKEY: '3Zumf1xFdfiHXKuUgLufCfO6VU77DSHEGkSFTJonid3F0WUTVLlfBF5NY6M9GUNQ',  // Replace with your actual API key
  APISECRET: 'zOTf6xuhYl0ZCSPXYoxydPAbpQCOLK8Cz6uWp4Os80E8Ilv5ryCtUj33NSFUXDkGT', // Replace with your actual API secret
  test: true, // Enable testnet
});

// Endpoint to fetch and store Binance data
app.get('/api/binanceData', async (req, res) => {
  try {
    binance.prices(async (error, ticker) => {
      if (error) {
        return res.status(500).send(error);
      }

      const symbols = Object.keys(ticker);

      for (const symbol of symbols) {
        const price = ticker[symbol];
        const newData = new BinanceData({
          symbol: symbol,
          price: price,
          timestamp: new Date(),
        });
        await newData.save();
      }

      res.send('Binance data stored successfully');
    });
  } catch (error) {
    console.error('Error fetching and storing Binance data:', error);
    res.status(500).send('Error fetching and storing Binance data');
  }
});

app.listen(port, () => console.log(`Server listening on port ${port}`));
