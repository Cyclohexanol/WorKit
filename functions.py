import math
import json
import sqlite3
from WorKit import *

def format_json(json_format, entries):
  entries_list = []
  for e in entries:
      entries_dict = {}
      for i in range(len(json_format)):
          entries_dict[json_format[i]] = e[i]
      entries_list.append(entries_dict);
  return entries_list

def insert_into_DB(query):
    db = get_db()
    db.execute(query)
    db.commit()

def fetch_from_DB(json_format, query):
    cursor = get_db().cursor()
    cursor.execute(query)
    entries = cursor.fetchall()
    result = format_json(json_format, entries)
    return json.dumps(result)

def insertGateway(gateway_id, gateway_building):
    query = "INSERT INTO gateways VALUES (" + gateway_id + ", " + gateway_building + ");"
    insert_into_DB(query)

def insertButtonID(button_id, team_name, worker_id):
    query = "UPDATE workers SET button_id = 's'" + button_id + "' WHERE team_name = " + team_name +" AND id = '" + worker_id + "');"
    insert_into_DB(query)

def insertMovementID(movement_id, team_name, worker_id):
    query = "UPDATE workers SET movement_id = ''" + movement_id + "' WHERE team_name = " + team_name +" AND id = '" + worker_id + "');"
    insert_into_DB(query)

def insertProximityID(proximity_id, team_name, worker_id):
    query = "UPDATE workers SET proximity_id = ''" + proximity_id + "' WHERE team_name = " + team_name +" AND id = '" + worker_id + "');"
    insert_into_DB(query)

def insertTemperatureID(temperature_id, team_name, worker_id):
    query = "UPDATE workers SET temperature_id = ''" + temperature_id + "' WHERE team_name = " + team_name +" AND id = '" + worker_id + "');"
    insert_into_DB(query)

def insertButtonLog(time, worker_id):
    query = "SELECT COUNT(*) FROM button_log;"
    json_format = ['count']
    id = int(fetch_from_DB(json_format, query)['count'][0]) + 1
    query = "INSERT INTO button_log VALUES (" + id + ", " + worker_id + ", " + time + ");"
    insert_into_DB(query)

def insertMovementLog(time, worker_id, movement):
    query = "SELECT COUNT(*) FROM movement_log;"
    json_format = ['count']
    id = int(fetch_from_DB(json_format, query)['count'][0]) + 1
    query = "INSERT INTO movement_log VALUES (" + id + ", " + worker_id + ", " + time + ", " + movement + ");"
    insert_into_DB(query)

def insertTemperatureLog(time, worker_id, temperature):
    query = "SELECT COUNT(*) FROM temperature_log;"
    json_format = ['count']
    id = int(fetch_from_DB(json_format, query)['count'][0]) + 1
    query = "INSERT INTO temperature_log VALUES (" + id + ", " + worker_id + ", " + time + ", " + temperature + ");"
    insert_into_DB(query)

def insertProximityLog(time, worker_id, gateway_id):
    query = "SELECT COUNT(*) FROM proximity_log;"
    json_format = ['count']
    id = int(fetch_from_DB(json_format, query)['count'][0]) + 1
    query = "INSERT INTO proximity_log VALUES (" + id + ", " + worker_id + ", " + time + ", " + gateway_id + ");"
    insert_into_DB(query)

def insertMessageLog(time, worker_id, sentiment):
    query = "SELECT COUNT(*) FROM proximity_log;"
    json_format = ['count']
    result = fetch_from_DB(json_format, query)['count'][0]
    print(result)
    id = int(fetch_from_DB(json_format, query)['count'][0]) + 1
    query = "INSERT INTO proximity_log VALUES (" + id + ", " + worker_id + ", " + time + ", " + sentiment + ");"
    insert_into_DB(query)

def fetchButtonLogInInterval(start, end, worker_id):
    query = "SELECT timestamp FROM button_log WHERE worker_id = '" + worker_id + "' AND timestamp > " + start + " AND timestamp < " + end + ";)"
    json_format = ['timestamp']
    return fetch_from_DB(json_format, query)

def fetchTemperatureLogInInterval(start, end, worker_id):
    query = "SELECT timestamp, temperature_log WHERE worker_id = '" + worker_id + "' AND timestamp > " + start + " AND timestamp < " + end + ";)"
    json_format = ['timestamp']
    return fetch_from_DB(json_format, query)

def fetchProximityLogInInterval(start, end, worker_id):
    query = "SELECT proximity_log.timestamp, gateways.building FROM proximity_log, gateways WHERE worker_id = '" + worker_id + "' AND timestamp > " + start + " AND timestamp < " + end + ";)"
    json_format = ['timestamp', 'building']
    return fetch_from_DB(json_format, query)

def fetchMovementLogInInterval(start, end, worker_id):
    query = "SELECT timestamp FROM movement_id WHERE worker_id = '" + worker_id + "' AND timestamp > " + start + " AND timestamp < " + end + ";)"
    json_format = ['timestamp']
    return fetch_from_DB(json_format, query)

def fetchMessageLogInInterval(start, end, worker_id):
    query = "SELECT timestamp, message_log WHERE message_log.worker_id = '" + worker_id + "' AND timestamp > " + start + " AND timestamp < " + end + ";)"
    json_format = ['timestamp', 'sentiment']
    return fetch_from_DB(json_format, query)

def sentimentStats(start, end, worker_id):
    query = "SELECT AVG(sentiment), MAX(sentiment), MIN(sentiment) FROM message_log WHERE message_log.worker_id = '" + worker_id + "' AND timestamp > " + start + " AND timestamp < " + end + ";)"
    json_format = ['avg', 'max', 'min']
    return fetch_from_DB(json_format, query)

def temperatureStats(start, end, worker_id):
    query = "SELECT AVG(temperature), MAX(temperature), MIN(temperature) FROM temperature_log WHERE message_log.worker_id = '" + worker_id + "' AND timestamp > " + start + " AND timestamp < " + end + ";)"
    json_format = ['avg', 'max', 'min']
    return fetch_from_DB(json_format, query)

def buttonCount(start, end, worker_id):
    query = "SELECT COUNT(*) FROM button_log WHERE worker_id = '" + worker_id + "' AND timestamp > " + start + " AND timestamp < " + end + ";)"
    json_format = ['count']
    return fetch_from_DB(json_format, query)
