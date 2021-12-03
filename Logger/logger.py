import os
import logging
import logging.handlers
from Config.settings import config

# search settings from config
path = config.path() + config.settings("Logger", "FILE_PATH")
filename = config.path() + config.settings("Logger", "FILE_PATH") + config.settings("Logger", "FILE_NAME")
maxBytes = config.settings("Logger", "MAX_BYTES")
backupCount = config.settings("Logger", "AMOUNT")
clearUp = config.settings("Logger", "CLEAR_UP")
colorful = config.settings("Logger", "COLORFUL")

# create a logger，create a list to save logger data
logger = logging.getLogger()
logger_records = []


class CustomFilter(logging.Filter):
    def filter(self, record):
        # logger_records.append(record.msg)
        return record.msg


def clearUpLogFile():
    if not os.path.exists(path):
        os.mkdir(path)
    with open(filename, "w") as file:
        file.seek(0)
        file.truncate()  # clear file


def logger_init():
    # clear logger file
    if clearUp:
        clearUpLogFile()

    # set logger output level
    logger.setLevel(logging.INFO)
    filter = CustomFilter()
    logger.addFilter(filter)

    # set logger output style
    # fmt = logging.Formatter('%(asctime)s - %(process)d-%(threadName)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    if colorful:
        colorFmt = "\033[34m[%(asctime)s]\033[0m \033[36m(%(module)s.%(funcName)s):\033[0m \033[33m<%(levelname)s>\033[0m \033[32m%(message)s\033[0m"
    else:
        fmt = '[%(asctime)s] (%(module)s.%(funcName)s): <%(levelname)s> %(message)s'
    datefmt = "%Y-%m-%d %H:%M:%S"
    formatter = logging.Formatter(fmt=colorFmt, datefmt=datefmt)

    # define a console_handler for console output
    console_handler = logging.StreamHandler()

    # define a console_handler for console output
    file_handler = logging.handlers.RotatingFileHandler(
        filename, maxBytes=maxBytes, backupCount=backupCount, encoding="utf-8")

    # add formatter for handler
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    #  add initialized handler object to logger object
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


logger_init()
