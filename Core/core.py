import random
import time
from Logs.logs import log
from Settings.settings import SERVER_HOST, LOCAL_HOST, PORT, DEBUG
from Server.server import server
from threading import Thread


def main():
    server()

def core():
    thread_server = Thread(target=server)
    thread_server.start()
