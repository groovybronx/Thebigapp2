from flask import Flask
from binance.client import Client
import os
from pymongo import MongoClient
import datetime

app = Flask(__name__)

# Binance API credentials (replace with your actual keys)
api_key = os.environ.get('BINANCE_API')
api_secret = os.environ.get('BINANCE_SECRET')

client = Client(api_key, api_secret, testnet=True)

# MongoDB setup
mongo_client = MongoClient('mongodb://mongodb:27017/')  # Use 'mongodb' as hostname
db = mongo_client.binanceData

@app.route('/api/binanceData')
def get_binance_data():
    try:
        prices = client.get_all_tickers()
        for ticker in prices:
            ticker['timestamp'] = datetime.datetime.utcnow()
            db.prices.insert_one(ticker)
        return "Binance data stored successfully"
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)