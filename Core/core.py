from Storage import storage
from Config import config
from Message import message
from Logger import logger, progress


def main():
    # start code
    logger.info("===== write code here =====")
    logger.info({config.Information.project, config.Information.version})
    message.user("hello user", 1462648167)
    message.group("hello group", 791031608)
    progress(10)


