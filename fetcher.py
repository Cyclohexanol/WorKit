import WorKit
from slackclient import SlackClient

sc = SlackClient(WorKit.app_token)

def loop():
    if sc.rtm_connect():
        while True:
            interpret(sc.rtm_read())
            time.sleep(1)
    else:
        print("Connection Failed, invalid token?")

def interpret(message):
    print(message['text'])
    return NULL
