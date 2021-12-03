from Server.api import log, serverConfig, signIn


def urls(url, request):
    if (url == "/log"):
        return log(request)
    elif (url == "/config"):
        return serverConfig(request)
    elif (url == "/sign-in"):
        return signIn(request)
    else:
        return "No Response"
