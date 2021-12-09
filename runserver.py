from concurrent.futures import ProcessPoolExecutor
from Core import core
from Logger import logger
from Scheduler import Timer
from Config import config
from Server import server
from threading import Thread


def running():
    PROCESS_MODEL = config.Server.PROCESS_MODEL
    SCHEDULER = config.Scheduler.START_USING
    SERVER = config.Server.START_USING
    if not SCHEDULER:
        thread_core = Thread(target=core)
        thread_core.start()
    else:  # 调度器开启后core函数将被scheduler调度器代理，开启定时执行core
        startTime = config.Scheduler.START_TIME
        skipWeekend = config.Scheduler.SKIP_WEEKEND
        scheduler = Timer(task=core, startTime=startTime, skipWeekend=skipWeekend)
        thread_scheduler = Thread(target=scheduler.schedule)
        thread_scheduler.start()
    if SERVER:
        if PROCESS_MODEL:
            work_count = config.Server.PROCESS_COUNT
            server_process(work_count)
        else:
            thread_server = Thread(target=server)
            thread_server.start()


def server_process(work_count=4):
    with ProcessPoolExecutor(work_count) as pool:
        for i in range(work_count):
            pool.submit(server())


if __name__ == "__main__":
    DEBUG = config.Debug.DEBUG
    if DEBUG:
        logger.info("\n===== DEBUG MODE =====")
        core()
    else:
        running()
