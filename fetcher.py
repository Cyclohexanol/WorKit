import json
import time
import WorKit
import datetime
import requests
import functions
from slackclient import SlackClient
from flask import Flask, g, jsonify, request, redirect

sc = SlackClient(WorKit.bot_token)
temperature = sensor("EMSENSORDEVICEFORMAT00000001", "temperature")
delta = datetime.timedelta(0, 30, 0)

#LOOPS
def loop():
    message_loop()

def message_loop():
    if sc.rtm_connect():
        while True:
            message = sc.rtm_read()
            interpret(message)
            time.sleep(1)
    else:
        print("Connection Failed, invalid token?")

def data_loop():
    while True:
        get_sensor_data(temperature, datetime.datetime.now())
        time.sleep(30)

#DATA_PROCESSING
def interpret(message):
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
            sentiment = r.json()['documents'][0]['score']
            worker_id = message[0]['user']
            time = message[0]['ts']

            functions.insertMessageLog(time, worker_id, sentiment)

def get_sensor_data(sensor, datetime):
    headers = {"token":"saEbYNtHbxZ6ThHE"}
    url = "lauzhack.ael.li/events/uuid/:uuid/type/:type/minor/:minor/date/:from?/:to?=2016-12-00T00:00:00.0000"
    sensor_minor = 0
    params = {"uuid":sensor.uuid, "type":sensor.sensor_type, "minor":sensor_minor, "from":(datetime - delta), "/:to?":datetime}
