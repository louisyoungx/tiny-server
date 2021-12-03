import copy

from Config.settings import config


def log(request):
    file_path = config.path() + config.settings("Logger", "FILE_PATH") + config.settings("Logger", "FILE_NAME")
    file_page_file = open(file_path, 'r')
    return str(file_page_file.read())


def serverConfig(request):
    appConfig = copy.deepcopy(config._config._sections)
    for model in appConfig:
        for item in appConfig[model]:
            appConfig[model][item] = eval(appConfig[model][item])
            value = appConfig[model][item]
            # DEBUG print(model, item, value, type(value))
    return appConfig
