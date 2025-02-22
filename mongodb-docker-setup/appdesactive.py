from pymongo import MongoClient
from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()  # Charge les variables depuis .env

# MongoDB Configuration
MONGODB_HOST = 'mongodb'
MONGODB_PORT = 27017
MONGODB_DATABASE = 'binance_data'

# Binance API Keys (Replace with your actual keys)

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")

def connect_to_mongodb():
    """Connects to MongoDB."""
    try:
        client = MongoClient(f'mongodb://{MONGODB_HOST}:{MONGODB_PORT}/')
        db = client[MONGODB_DATABASE]
        print("Connected to MongoDB")
        return db
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None

def connect_to_binance():
    """Connects to Binance API."""
    try:
        client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)
        print("Connected to Binance")
        return client
    except Exception as e:
        print(f"Error connecting to Binance: {e}")
        return None

def main():
    """Main function to connect to MongoDB and Binance."""
    db = connect_to_mongodb()
    binance_client = connect_to_binance()

    if db and binance_client:
        # Example: Fetching account information
        try:
            account = binance_client.get_account()
            print("Account Information:", account)
        except Exception as e:
            print(f"Error fetching account information: {e}")

if __name__ == "__main__":
    main()
