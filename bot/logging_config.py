import logging

# Configure logging for the trading bot
logger = logging.getLogger('trading_bot')
logger.setLevel(logging.INFO)

# File handler for trading.log
file_handler = logging.FileHandler('trading.log')
file_handler.setLevel(logging.INFO)

# Formatter for log messages
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add handler if not already added
if not logger.hasHandlers():
    logger.addHandler(file_handler)
else:
    # Avoid duplicate handlers in some environments
    logger.handlers.clear()
    logger.addHandler(file_handler)
