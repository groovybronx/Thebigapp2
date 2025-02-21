import os
from pymongo import MongoClient
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()  # Charge les variables depuis .env

# Configuration MongoDB (Docker)
MONGODB_HOST = os.getenv("MONGODB_HOST", "mongodb")  # Nom du service Docker
MONGODB_PORT = int(os.getenv("MONGODB_PORT", 27017))
MONGODB_USER = os.getenv("MONGODB_USER", "admin")
MONGODB_PASS = os.getenv("MONGODB_PASS", "pass")
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE", "binance_data")

# Configuration Binance
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")

def connect_to_mongodb():
    """Connexion à MongoDB avec authentification"""
    try:
        client = MongoClient(
            host=MONGODB_HOST,
            port=MONGODB_PORT,
            username=MONGODB_USER,
            password=MONGODB_PASS
        )
        db = client[MONGODB_DATABASE]
        print("✅ Connecté à MongoDB")
        return db
    except Exception as e:
        print(f"❌ Erreur MongoDB: {e}")
        return None