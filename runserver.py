from Core.core import main
from Logger.logger import logger
from Scheduler.scheduler import schedule
from Config.settings import config
from Server.server import server
from threading import Thread
from concurrent.futures import ProcessPoolExecutor

def running():
    PROCESS_MODEL = config.settings("Server", "PROCESS_MODEL")
    SCHEDULER = config.settings("Scheduler", "START_USING")
    if SCHEDULER == False:
        thread_main = Thread(target=main)
        thread_main.start()
    else: # 调度器开启后main函数将被scheduler调度器代理，开启定时执行main
        thread_scheduler = Thread(target=schedule)
        thread_scheduler.start()
    if PROCESS_MODEL:
        work_count = config.settings("Server", "PROCESS_COUNT")
        server_process(work_count)
    else:
        thread_server = Thread(target=server)
        thread_server.start()

def server_process(work_count=4):
    with ProcessPoolExecutor(work_count) as pool:
        for i in range(work_count):
            pool.submit(server())

if __name__ == "__main__":
    DEBUG = config.settings("Debug", "DEBUG")
    if DEBUG == True:
        logger.info("\n===== DEBUG MODE =====")
        main()
    else:
        running()

