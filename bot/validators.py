def validate_order_params(symbol, side, order_type, quantity, price=None):
    """
    Validate order parameters for Binance Futures orders.
    Raises ValueError with clear message if invalid.
    """
    # Symbol: non-empty string
    if not isinstance(symbol, str) or not symbol.strip():
        raise ValueError('Symbol must be a non-empty string.')

    # Side: BUY or SELL only
    if side not in ('BUY', 'SELL'):
        raise ValueError("Side must be 'BUY' or 'SELL'.")

    # Order type: MARKET or LIMIT
    if order_type not in ('MARKET', 'LIMIT'):
        raise ValueError("Order type must be 'MARKET' or 'LIMIT'.")

    # Quantity: must be > 0
    try:
        qty = float(quantity)
        if qty <= 0:
            raise ValueError
    except Exception:
        raise ValueError('Quantity must be a number greater than 0.')

    # Price: required for LIMIT, must be > 0
    if order_type == 'LIMIT':
        if price is None:
            raise ValueError('Price is required for LIMIT orders.')
        try:
            prc = float(price)
            if prc <= 0:
                raise ValueError
        except Exception:
            raise ValueError('Price must be a number greater than 0 for LIMIT orders.')
