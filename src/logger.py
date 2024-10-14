# Importing packages
import logging
import os
from datetime import datetime

# Creating the format in which events will be logged
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Creating the logs directory for the project
logs_path = os.path.join(os.getcwd(), 'logs')
os.makedirs(logs_path, exist_ok=True)

# Joining the logs directory path and logs file to create the log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Overriding the basicConfig of the logging package to include the new
# log file format and path
logging.basicConfig(
    filename='LOG_FILE_PATH',
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
