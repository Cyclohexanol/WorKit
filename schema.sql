"""drop table if exists workers;
create table workers(
  id INTEGER NOT NULL PRIMARY KEY,
  team_name TEXT NOT NULL,
  button_id TEXT UNIQUE,
  proximity_id TEXT UNIQUE,
  temperature_id TEXT UNIQUE,
  movement_id TEXT UNIQUE
);

drop table if exists gateways:
create table gateways(
  id TEXT NOT NULL PRIMARY KEY,
  building TEXT
);

drop table if exists message_log;
create table message_log(
  id INTEGER NOT NULL PRIMARY KEY,
  worker_id INTEGER NOT NULL,
  timestamp INTEGER,
  sentiment REAL,
  FOREIGN KEY(worker_id) REFERENCES workers(id)
);

drop table if exists temperature_log;
create table temperature_log(
  id INTEGER NOT NULL PRIMARY KEY,
  worker_id INTEGER NOT NULL,
  timestamp INTEGER,
  temperature REAL,
  FOREIGN KEY(worker_id) REFERENCES workers(id)
);

drop table if exists button_log;
create table button_log(
  id INTEGER NOT NULL PRIMARY KEY,
  worker_id INTEGER NOT NULL,
  timestamp INTEGER,
  FOREIGN KEY(worker_id) REFERENCES workers(id)
);

drop table if exists proximity_log;
create table proximity_log(
  id INTEGER NOT NULL PRIMARY KEY,
  worker_id INTEGER NOT NULL,
  timestamp INTEGER,
  gateway_id TEXT NOT NULL,
  FOREIGN KEY(gateway_id) REFERENCES gateways(id),
  FOREIGN KEY(worker_id) REFERENCES workers(id)
);

drop table if exists movement_log;
create table movement_log(
  id INTEGER NOT NULL PRIMARY KEY,
  worker_id INTEGER NOT NULL,
  timestamp INTEGER,
  movement INTEGER,
  FOREIGN KEY(worker_id) REFERENCES workers(id)
);"""
