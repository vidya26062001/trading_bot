def validate_side(side):
    if side not in ("BUY", "SELL"):
        raise ValueError("side must be BUY or SELL")

def validate_order_type(order_type):
    if order_type not in ("MARKET", "LIMIT"):
        raise ValueError("order_type must be MARKET or LIMIT")

def validate_quantity(quantity):
    if quantity <= 0:
        raise ValueError("quantity must be > 0")

def validate_price(price):
    if price <= 0:
        raise ValueError("price must be > 0")
