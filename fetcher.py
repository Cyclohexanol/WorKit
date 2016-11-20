import time
import requests
from WorKit import *
from slackclient import SlackClient
from flask import Flask, g, jsonify, request, redirect

sc = SlackClient(bot_token)

def loop():
    if sc.rtm_connect():
        while True:
            interpret(sc.rtm_read())
            time.sleep(1)
    else:
        print("Connection Failed, invalid token?")

def interpret(input):
    with app.app_context() and app.test_request_context():
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

                r = requests.post("https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment", data=json, headers=headers)

        return None
