import logging
import os
from datetime import datetime
 
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #naming template of file
logs_path = os.path.join(os.getcwd(),"logs")
os.makedirs(logs_path, exist_ok=True) #exist_ok = true will allow to keep appending files even if foler/file exists

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    level = logging.INFO,
    format = '[%(asctime)s]%(lineno)d %(name)s - %(levelname)s - %(message)s' #this is the format of the content in the log file
)

# if __name__ == "__main__":
#     logging.info("Logging started") # =>lineno is 18

    