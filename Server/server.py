from http.server import HTTPServer
from Logger import logger
from Server import RequestHandler
from Config import config


def server():
    NAME = config.Server.SERVER_NAME
    VERSION = config.Server.SERVER_VERSION
    DEBUG = config.Debug.DEBUG
    LOCAL_HOST = config.Server.LOCAL_HOST
    SERVER_HOST = config.Server.SERVER_HOST
    PORT = config.Server.PORT
    if DEBUG:
        name = LOCAL_HOST
    else:
        name = SERVER_HOST
    port = PORT
    host = LOCAL_HOST
    serverAddress = (host, port)
    logger.info("{}-{}".format(NAME, VERSION))
    logger.info("http://{}:{}/".format(name, port))
    httpServer = HTTPServer(serverAddress, RequestHandler)
    httpServer.serve_forever()
