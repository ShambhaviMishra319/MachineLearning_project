import logging
import os
from datetime import datetime

# Create a log file with a timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the directory to store logs
logs_path = os.path.join(os.getcwd(), "logs",LOG_FILE)  # 'logs' directory in the current working directory
os.makedirs(logs_path, exist_ok=True)  # Create the directory if it doesn't exist

# Full path of the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Example log message
logging.info("Logging setup complete!")
