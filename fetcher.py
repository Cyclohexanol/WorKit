import WorKit
from slackclient import SlackClient

sc = SlackClient(WorKit.token)

if sc.rtm_connect():
    while True:
        interpret(sc.rtm_read())
        time.sleep(1)
else:
    print("Connection Failed, invalid token?")

def interpret(message):
    console.log(message['text'])
    return NULL
