import copy

from Config.settings import _config_, config


def log(request):
    file_path =config.path() + config.Logger.FILE_PATH + config.Logger.FILE_NAME
    file_page_file = open(file_path, 'r')
    return str(file_page_file.read())


def serverConfig(request):
    return _config_.menu()


def signIn(request):
    # POST example
    username = request["username"]
    password = request["password"]
    return "success"
