import argparse
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_order_params
from bot.logging_config import logger
import sys

try:
    from colorama import Fore, Style, init as colorama_init
    colorama_init()
    COLOR = True
except ImportError:
    COLOR = False

def print_colored(text, color=None):
    if COLOR and color:
        print(color + text + Style.RESET_ALL)
    else:
        print(text)

def main():
    parser = argparse.ArgumentParser(
        description='Binance Futures Trading Bot (Testnet)'
    )
    parser.add_argument('--symbol', required=True, help='Trading symbol, e.g., BTCUSDT')
    parser.add_argument('--side', required=True, choices=['BUY', 'SELL'], help='Order side (BUY or SELL)')
    parser.add_argument('--type', required=True, choices=['MARKET', 'LIMIT'], help='Order type (MARKET or LIMIT)')
    parser.add_argument('--quantity', required=True, type=float, help='Order quantity (> 0)')
    parser.add_argument('--price', type=float, help='Order price (required for LIMIT)')
    args = parser.parse_args()

    try:
        # Validate params (extra validation for CLI)
        validate_order_params(args.symbol, args.side, args.type, args.quantity, args.price)
        if args.type == 'MARKET':
            result = place_market_order(args.symbol, args.side, args.quantity)
        else:
            result = place_limit_order(args.symbol, args.side, args.quantity, args.price)
        # Print order summary
        summary = f"\nOrder Placed Successfully!\n" \
                  f"Order ID   : {result.get('orderId')}\n" \
                  f"Status     : {result.get('status')}\n" \
                  f"ExecutedQty: {result.get('executedQty')}\n" \
                  f"Avg Price  : {result.get('avgPrice', 'N/A')}\n"
        print_colored(summary, Fore.GREEN if COLOR else None)
    except Exception as e:
        logger.error(f"Error: {e}")
        print_colored(f"\nError: {e}\n", Fore.RED if COLOR else None)
        sys.exit(1)

if __name__ == '__main__':
    main()
