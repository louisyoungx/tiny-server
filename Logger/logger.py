import logging
import logging.handlers
from Config.settings import config

logger_records = []
filename = config.settings("Logger", "FILE_NAME")
maxBytes = config.settings("Logger", "MAX_BYTES")
backupCount = config.settings("Logger", "AMOUNT")
filename = config.path() + config.settings("Logger", "FILE_PATH") +filename
logger = logging.getLogger()

class CustomFilter(logging.Filter):
    def filter(self, record):
        logger_records.append(record.msg)
        return record.msg

def logger_init():
    logger.setLevel(logging.INFO)
    filter = CustomFilter()
    logger.addFilter(filter)
    # formatter = logging.Formatter('%(asctime)s - %(process)d-%(threadName)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    fmt = '[%(asctime)s] (%(module)s.%(funcName)s): <%(levelname)s> %(message)s'
    datefmt = "%Y-%m-%d %H:%M:%S"
    formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    file_handler = logging.handlers.RotatingFileHandler(
        filename, maxBytes=maxBytes, backupCount=backupCount, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


logger_init()



