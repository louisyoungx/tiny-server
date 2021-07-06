from Settings.settings import DEBUG
from Core.core import main, core
from Logs.logs import log

if __name__ == "__main__":
    if DEBUG == True:
        log.update("Core", "===== DEBUG MODE =====")
        main()
    else:
        core()