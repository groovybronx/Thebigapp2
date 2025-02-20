from binance.client import Client

def get_binance_client():
    api_key = 'YOUR_API_KEY'
    api_secret = 'YOUR_API_SECRET'
    return Client(api_key, api_secret)