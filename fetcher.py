import time
import WorKit
from slackclient import SlackClient

sc = SlackClient(WorKit.bot_token)

def loop():
    if sc.rtm_connect():
        while True:
            interpret(sc.rtm_read())
            time.sleep(1)
    else:
        print("Connection Failed, invalid token?")

def interpret(message):
    if message.__len__() != 0:
        print(message[0])
    return None
