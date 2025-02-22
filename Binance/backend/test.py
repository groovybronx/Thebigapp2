from binance.client import Client
import os
from dotenv import load_dotenv
import logging

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Binance API credentials
api_key = os.environ.get('BINANCE_API_KEY')
api_secret = os.environ.get('BINANCE_API_SECRET')

if not api_key or not api_secret:
    logger.error("Binance API keys not found in .env file.")
    exit(1)

try:
    client = Client(api_key, api_secret, testnet=True) # change testnet=False if you use real account
    response = client.ping()
    logger.info(f"Binance API connection successful: {response}")
except Exception as e:
    logger.error(f"Binance API connection failed: {e}")