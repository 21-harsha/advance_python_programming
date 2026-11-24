import logging

# Configure the logger
logger = logging.getLogger("MyLogger")
logger.setLevel(logging.DEBUG)

# Create handlers
file_handler = logging.FileHandler("app.log")
console_handler = logging.StreamHandler()

# Set levels for handlers
file_handler.setLevel(logging.DEBUG)
console_handler.setLevel(logging.INFO)

# Create formatters
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Add formatters to handlers
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Add logging messages
logger.debug("This is a debug message")
logger.info("This is an information message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")

print("Logging completed.")
