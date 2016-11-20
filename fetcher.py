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

def interpret(input):
    if input.__len__() != 0:
        message = input[0]
        if 'text' in message:
            headers = {"Ocp-Apim-Subscription-Key":"3cbc1873c0e847a8b951fab2e549a86a",
                "Content-Type":"application/json", "Accept":"application/json"}
            json = jsonify({
                "documents": [{
                    "language": "en",
                    "id": "1",
                    "text": message['text']
                }]
            })

            r = requests.post("https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment", json, headers)

    return None
