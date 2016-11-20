import json
import time
import WorKit
import requests
from slackclient import SlackClient
from flask import Flask, g, jsonify, request, redirect

sc = SlackClient(WorKit.bot_token)

def loop():
    if sc.rtm_connect():
        while True:
            message = sc.rtm_read()
            interpret(message)
            time.sleep(1)
    else:
        print("Connection Failed, invalid token?")

def interpret(input):
    message = input
    if message.__len__() != 0:
        if 'text' in message[0]:
            headers = {"Ocp-Apim-Subscription-Key":"3cbc1873c0e847a8b951fab2e549a86a",
                "Content-Type":"application/json", "Accept":"application/json"}
            data = json.dumps({
                "documents": [{
                    "language": "en",
                    "id": "123456",
                    "text": message[0]['text']
                }]
            })
            r = requests.post("https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment", data=data, headers=headers)
        return None
