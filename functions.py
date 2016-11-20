import math
import sqlite3
from WorKit import *

def insertGateway(gateway_id, gateway_building):
    WorKit.rv.execute("INSERT INTO gateways VALUES (" + gateway_id + ", " + gateway_building + ");")

def insertButtonID(button_id, team_name, worker_id):
    WorKit.rv.execute("UPDATE workers SET button_id = 's'" + button_id + "' WHERE team_name = " + team_name +" AND id = '" + worker_id + "');")

def insertMovementID(movement_id, team_name, worker_id):
    WorKit.rv.execute("UPDATE workers SET movement_id = ''" + movement_id + "' WHERE team_name = " + team_name +" AND id = '" + worker_id + "');")

def insertProximityID(proximity_id, team_name, worker_id):
    WorKit.rv.execute("UPDATE workers SET proximity_id = ''" + proximity_id + "' WHERE team_name = " + team_name +" AND id = '" + worker_id + "');")

def insertTemperatureID(temperature_id, team_name, worker_id):
    WorKit.rv.execute("UPDATE workers SET temperature_id = ''" + temperature_id + "' WHERE team_name = " + team_name +" AND id = '" + worker_id + "');")

def insertButtonLog(time, worker_id):
    id = WorKit.rv.execute("SELECT COUNT(*) FROM button_log;")[0][0] + 1
    WorKit.rv.execute("INSERT INTO button_log VALUES (" + id + ", " + worker_id + ", " + time + ");")

def insertMovementLog(time, worker_id, movement):
    id = WorKit.rv.execute("SELECT COUNT(*) FROM movement_log;")[0][0] + 1
    WorKit.rv.execute("INSERT INTO movement_log VALUES (" + id + ", " + worker_id + ", " + time + ", " + movement + ");")

def insertTemperatureLog(time, worker_id, temperature):
    id = WorKit.rv.execute("SELECT COUNT(*) FROM temperature_log;")[0][0] + 1
    WorKit.rv.execute("INSERT INTO temperature_log VALUES (" + id + ", " + worker_id + ", " + time + ", " + temperature + ");")

def insertProximityLog(time, worker_id, gateway_id):
    id = WorKit.rv.execute("SELECT COUNT(*) FROM proximity_log;")[0][0] + 1
    WorKit.rv.execute("INSERT INTO proximity_log VALUES (" + id + ", " + worker_id + ", " + time + ", " + gateway_id + ");")

def insertMessageLog(time, worker_id, sentiment):
    id = WorKit.rv.execute("SELECT COUNT(*) FROM proximity_log;")[0][0] + 1
    WorKit.rv.execute("INSERT INTO proximity_log VALUES (" + id + ", " + worker_id + ", " + time + ", " + sentiment + ");")

def fetchButtonLogInInterval(start, end, worker_id):
    WorKit.rv.execute("SELECT timestamp FROM button_log WHERE worker_id = '" + worker_id + "' AND timestamp > " + start + " AND timestamp < " + end + ";)")

def fetchTemperatureLogInInterval(start, end, worker_id):
    WorKit.rv.execute("SELECT timestamp, temperature_log WHERE worker_id = '" + worker_id + "' AND timestamp > " + start + " AND timestamp < " + end + ";)")

def fetchProximityLogInInterval(start, end, worker_id):
    WorKit.rv.execute("SELECT proximity_log.timestamp, gateways.building FROM proximity_log, gateways WHERE worker_id = '" + worker_id + "' AND timestamp > " + start + " AND timestamp < " + end + ";)")

def fetchMovementLogInInterval(start, end, worker_id):
    WorKit.rv.execute("SELECT timestamp FROM movement_id WHERE worker_id = '" + worker_id + "' AND timestamp > " + start + " AND timestamp < " + end + ";)")

def fetchMessageLogInInterval(start, end, worker_id):
    WorKit.rv.execute("SELECT timestamp, message_log WHERE message_log.worker_id = '" + worker_id + "' AND timestamp > " + start + " AND timestamp < " + end + ";)")

def sentimentStats(start, end, worker_id):
    WorKit.rv.execute("SELECT AVG(sentiment), MAX(sentiment), MIN(sentiment) FROM message_log WHERE message_log.worker_id = '" + worker_id + "' AND timestamp > " + start + " AND timestamp < " + end + ";)")

def temperatureStats(start, end, worker_id):
    WorKit.rv.execute("SELECT AVG(temperature), MAX(temperature), MIN(temperature) FROM temperature_log WHERE message_log.worker_id = '" + worker_id + "' AND timestamp > " + start + " AND timestamp < " + end + ";)")

def buttonCount(start, end, worker_id):
    WorKit.rv.execute("SELECT COUNT(*) FROM button_log WHERE worker_id = '" + worker_id + "' AND timestamp > " + start + " AND timestamp < " + end + ";)")
