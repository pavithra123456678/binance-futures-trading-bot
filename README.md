# Binance Futures Trading Bot (Testnet)

A CLI-based trading bot for placing MARKET and LIMIT orders on Binance USDT-M Futures Testnet.


## Features
- Place MARKET and LIMIT orders via CLI
- Uses Binance Futures Testnet (safe for practice)
- Modular, clean Python 3.x code
- API keys loaded from .env file
- Logging to `trading.log`
- Input validation and error handling
- Handles errors such as invalid inputs, API failures, and insufficient balance gracefully
- Colored CLI output (if `colorama` installed)

## Requirements
- Python 3.8+

## Setup
1. **Clone the repository**
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Add your Binance Testnet API keys**
   - Copy `.env.example` to `.env` and fill in your keys:
     ```
     API_KEY=your_api_key
     API_SECRET=your_api_secret
     ```
   - Get keys from https://testnet.binancefuture.com

## Usage
Run the bot from terminal:

### Place a MARKET order
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### Place a LIMIT order
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 60000
```

- `--symbol`   : Trading pair (e.g., BTCUSDT)
- `--side`     : BUY or SELL
- `--type`     : MARKET or LIMIT
- `--quantity` : Order quantity (> 0)
- `--price`    : Required for LIMIT orders


## Sample Output

Order Summary:
{'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 0.001}

Order Response:
Order ID: 12345678
Status: FILLED
Executed Qty: 0.001

## Assumptions
- Binance Futures Testnet is used
- Small quantities may trigger "notional too small" errors
- API keys must be valid and active

## Notes
- This bot uses the Binance Futures Testnet (no real funds involved).
- All activity is logged to `trading.log`.
- For colored output, install `colorama` (optional).

## Disclaimer
This project is for educational and testing purposes only. Use at your own risk.
