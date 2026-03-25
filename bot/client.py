import os
from binance.client import Client
from dotenv import load_dotenv
from .logging_config import logger

# Load environment variables from .env file

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

if not API_KEY or not API_SECRET:
    logger.error('API_KEY and/or API_SECRET not set in environment.')
    raise ValueError('API_KEY and/or API_SECRET not set in environment.')

# Binance Futures Testnet base URL
BASE_URL = 'https://testnet.binancefuture.com'

class BinanceFuturesClient:
    def __init__(self):
        self.client = Client(API_KEY, API_SECRET, testnet=True)
        self.client.FUTURES_URL = BASE_URL
        logger.info('Initialized Binance Futures Client (Testnet)')

    def send_order(self, **order_params):
        """
        Wrapper to send an order to Binance Futures Testnet.
        Logs request and response.
        """
        logger.info(f"Sending order: {order_params}")
        try:
            response = self.client.futures_create_order(**order_params)
            logger.info(f"Order response: {response}")
            return response
        except Exception as e:
            logger.error(f"Order failed: {e}")
            raise
