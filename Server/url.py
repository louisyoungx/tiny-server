from Server.api import log, serverConfig


def urls(url, request):
    if (url == "/log"):
        return log(request)
    elif (url == "/config"):
        return serverConfig(request)
    else:
        return "No Response"
