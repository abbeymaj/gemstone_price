# Importing packages
import logging
import os
from datetime import datetime

# Creating the format in which events will be logged
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Creating the logs directory for the project
LOG_FILE_PATH = os.path.join('logs', LOG_FILE)
os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)

# Overriding the basicConfig of the logging package to include the new
# log file format and path
logging.basicConfig(
    filename='LOG_FILE_PATH',
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
