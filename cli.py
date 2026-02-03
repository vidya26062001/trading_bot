import argparse
import os
from dotenv import load_dotenv

from bot.client import BinanceFuturesClient
from bot.orders import place_market_order, place_limit_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)
from bot.logging_config import setup_logging

def main():
    setup_logging()
    load_dotenv()

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    validate_side(args.side)
    validate_order_type(args.type)
    validate_quantity(args.quantity)

    if args.type == "LIMIT":
        if args.price is None:
            raise ValueError("price is required for LIMIT orders")
        validate_price(args.price)

    client = BinanceFuturesClient(
        api_key=os.getenv("BINANCE_API_KEY"),
        api_secret=os.getenv("BINANCE_API_SECRET"),
    )

    print("\nOrder Request Summary")
    print(vars(args))

    if args.type == "MARKET":
        response = place_market_order(
            client, args.symbol, args.side, args.quantity
        )
    else:
        response = place_limit_order(
            client, args.symbol, args.side, args.quantity, args.price
        )

    print("\nOrder Response")
    print(f"Order ID     : {response.get('orderId')}")
    print(f"Status       : {response.get('status')}")
    print(f"Executed Qty : {response.get('executedQty')}")
    print(f"Avg Price    : {response.get('avgPrice', 'N/A')}")

    print("\n✅ Order placed successfully")

if __name__ == "__main__":
    main()
