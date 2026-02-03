from .client import BinanceFuturesClient

def place_market_order(client, symbol, side, quantity):
    return client.create_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity,
    )

def place_limit_order(client, symbol, side, quantity, price):
    return client.create_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        timeInForce="GTC",
        quantity=quantity,
        price=price,
    )
