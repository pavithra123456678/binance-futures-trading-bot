from .client import BinanceFuturesClient
from .validators import validate_order_params
from .logging_config import logger

def place_market_order(symbol, side, quantity):
    """
    Place a MARKET order on Binance Futures Testnet.
    Returns: dict with orderId, status, executedQty, avgPrice (if available)
    """
    validate_order_params(symbol, side, 'MARKET', quantity)
    client = BinanceFuturesClient()
    try:
        response = client.send_order(
            symbol=symbol,
            side=side,
            type='MARKET',
            quantity=quantity
        )
        return {
            'orderId': response.get('orderId'),
            'status': response.get('status'),
            'executedQty': response.get('executedQty'),
            'avgPrice': response.get('avgPrice', response.get('avgFillPrice', None))
        }
    except Exception as e:
        logger.error(f"Market order error: {e}")
        raise

def place_limit_order(symbol, side, quantity, price):
    """
    Place a LIMIT order on Binance Futures Testnet.
    Returns: dict with orderId, status, executedQty, avgPrice (if available)
    """
    validate_order_params(symbol, side, 'LIMIT', quantity, price)
    client = BinanceFuturesClient()
    try:
        response = client.send_order(
            symbol=symbol,
            side=side,
            type='LIMIT',
            quantity=quantity,
            price=price,
            timeInForce='GTC'
        )
        return {
            'orderId': response.get('orderId'),
            'status': response.get('status'),
            'executedQty': response.get('executedQty'),
            'avgPrice': response.get('avgPrice', response.get('avgFillPrice', None))
        }
    except Exception as e:
        logger.error(f"Limit order error: {e}")
        raise
