import json
import requests


class Message(object):
    def __init__(self):
        self.DEBUG = True
        self.URL = "www.louisyoung.site:8088"

    def sendFriendMessage(self, message, userid):

        path = "sendFriendMessage"
        URL = "http://{}/{}".format(self.URL, path)

        body = {
            "sessionKey": "YourSession",
            "target": userid,
            "messageChain": [
                {"type": "Plain", "text": message}
            ]
        }
        sender = requests.post(URL, data=json.dumps(body))

        mes = message.replace("\n", " ")
        if len(mes) > 10:
            mes = mes[:10] + "···"
        print("Send {}".format(mes))

        if self.DEBUG:
            print(sender.request.url)
            sender.raise_for_status()
            print(sender.text)

    def sendGroupMessage(self, message, groupid):

        path = "sendGroupMessage"
        URL = "http://{}/{}".format(self.URL, path)

        body = {
            "sessionKey": "YourSession",
            "target": groupid,
            "messageChain": [
                {"type": "Plain", "text": message}
            ]
        }
        sender = requests.post(URL, data=json.dumps(body))
        mes = message.replace("\n", " ")
        if len(mes) > 10:
            mes = mes[:10] + "···"
        print("Send {}".format(mes))

        if self.DEBUG:
            print(sender.request.URL)
            sender.raise_for_status()
            print(sender.text)

        return True


message = Message()


if __name__ == "__main__":
    message.sendFriendMessage("hello", 1462648167)
