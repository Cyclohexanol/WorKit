Insert a worker:
INSERT INTO workers VALUES(<WORKER_ID>, '<TEAM_NAME>', NULL, NULL, NULL, NULL);

Assign Sensor UUID to a worker with worker ID known and check team verification:
UPDATE workers SET button_id = '<SENSOR_ID>' WHERE team_name = 'TEAM_NAME' AND id = <WORKER_ID>;
UPDATE workers SET proximity_id = '<SENSOR_ID>' WHERE team_name = 'TEAM_NAME' AND id = <WORKER_ID>;
UPDATE workers SET temperature_id = '<SENSOR_ID>' WHERE team_name = 'TEAM_NAME' AND id = <WORKER_ID>;
UPDATE workers SET movement_id = '<SENSOR_ID>' WHERE team_name = 'TEAM_NAME' AND id = <WORKER_ID>;

!!!! NEED TO TURN ON THE FOREIGN KEYS:
PRAGMA foreign_keys = ON

Insert a gateway:
INSERT INTO gateways VALUES (<GATEWAY_ID>, <GATEWAY_NAME>);

Insert a log:
!!! TIMESTAMP is ? seconds from 01.01.1970
INSERT INTO message_log VALUES (<MESSAGE_ID>, <WORKER_ID>, <TIMESTAMP>, <SENTIMENT>);
INSERT INTO temperature_log VALUES (<TEMP_LOG_ID>, <WORKER_ID>, <TIMESTAMP>, <TEMPERATURE>);
INSERT INTO button_log VALUES (<B_LOG_ID>, <WORKER_ID>, <TIMESTAMP>);
INSERT INTO proximity_log VALUES(<PROX_ID>, <WORKER_ID>, <TIMESTAMP>, <GATEWAY_ID>);
INSERT INTO movement_log VALUES(<MOV_LOG>, <WORKER_ID>, <TIMESTAMP>, <MOVEMENT>);

!!! Consider semantics (<, >)!!!
Get general stats for sentiment of a worker from timestamp1 to timestamp2
SELECT AVG(sentiment), MAX(sentiment), MIN(sentiment) FROM message_log WHERE message_log.worker_id = <WORKER_ID> AND timestamp > <TIMESTAMP1> AND timestamp < <TIMESTAMP2>;

Get general stats for temperature for a worker from timestamp1 to timestamp2
SELECT AVG(temperature), MAX(temperature), MIN(temperature) FROM temperature_log WHERE worker_id = <WORKER_ID> AND timestamp > <TIMESTAMP1> AND timestamp < <TIMESTAMP2>;

Get count of button clicks for a worker from timestamp1 to timestamp2
SELECT COUNT(*) FROM button_log WHERE worker_id = <WORKER_ID> AND timestamp > <TIMESTAMP1> AND timestamp < <TIMESTAMP2>;

Log retrievals in (timestamp1, timestamp2) time period:
SELECT timestamp, sentiment FROM message_log WHERE message_log.worker_id = <WORKER_ID> AND timestamp > <TIMESTAMP1> AND timestamp < <TIMESTAMP2>;

SELECT timestamp, temperature FROM temperature_log WHERE worker_id = <WORKER_ID> AND timestamp > <TIMESTAMP1> AND timestamp < <TIMESTAMP2>;

SELECT timestamp FROM button_log WHERE worker_id = <WORKER_ID> AND timestamp > <TIMESTAMP1> AND timestamp < <TIMESTAMP2>;

SELECT proximity_log.timestamp, gateways.building FROM proximity_log, gateways WHERE worker_id = <WORKER_ID> AND timestamp > <TIMESTAMP1> AND timestamp < <TIMESTAMP2>;

SELECT timestamp, movement FROM movement_log WHERE worker_id = <WORKER_ID> AND timestamp > <TIMESTAMP1> AND timestamp < <TIMESTAMP2>;
