from Config import configInside, config


def serverLog(request):
    file_path = config.path() + config.Logger.FILE_PATH + config.Logger.FILE_NAME
    file_page_file = open(file_path, 'r')
    return str(file_page_file.read())


def serverConfig(request):
    return configInside.menu()


def signIn(request):
    # POST example
    username = request["username"]
    password = request["password"]
    return "success"
