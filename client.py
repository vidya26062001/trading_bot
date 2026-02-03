import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException

logger = logging.getLogger(__name__)

TESTNET_URL = "https://testnet.binancefuture.com"

class BinanceFuturesClient:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = TESTNET_URL

    def create_order(self, **kwargs):
        try:
            logger.info(f"Placing order request: {kwargs}")
            response = self.client.futures_create_order(**kwargs)
            logger.info(f"Order response: {response}")
            return response
        except (BinanceAPIException, BinanceRequestException) as e:
            logger.error(f"Binance API error: {e}")
            raise
        except Exception:
            logger.exception("Unexpected error")
            raise
