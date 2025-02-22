from binance.client import Client
import os
import datetime
from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
import logging

app = Flask(__name__)
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__) # Get the logger instance

logger.info("Starting the application...") # Log application start

# Binance API credentials
api_key = os.environ.get('BINANCE_API_KEY')
api_secret = os.environ.get('BINANCE_API_SECRET')

if not api_key or not api_secret:
    logger.error("Binance API keys not found in .env file.")
    exit(1)

client = Client(api_key, api_secret, testnet=True)

# MongoDB setup
mongo_client = MongoClient('mongodb://mongodb:27017/')
db = mongo_client.binanceData
logger.info("Connected to MongoDB.") # Log MongoDB connection

@app.route('/api/binanceData')
def get_binance_data():
    try:
        client.ping()
        logger.info("Binance API connection successful.")

        prices = client.get_all_tickers()
        logger.info(f"Retrieved {len(prices)} tickers from Binance.") # Log the number of tickers retrieved

        for ticker in prices:
            ticker['timestamp'] = datetime.datetime.now()
            try:
                db.prices.insert_one(ticker)
                logger.debug(f"Inserted ticker {ticker['symbol']} into MongoDB.") # Log each inserted ticker at DEBUG level
            except Exception as mongo_error:
                logger.error(f"Error inserting ticker {ticker['symbol']} into MongoDB: {mongo_error}")
                return "Error inserting data into MongoDB"

        logger.info("Binance data stored successfully.")
        return "Binance data stored successfully"
    except Exception as binance_error:
        logger.error(f"Binance API connection failed: {binance_error}")
        return "Binance API connection failed"

if __name__ == '__main__':
    logger.info("Starting Flask application...") # Log Flask start
    app.run(debug=True, host='0.0.0.0', port=5000)