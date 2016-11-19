"""drop table if exists workers;
create table workers(
  id INTEGER PRIMARY KEY,
  button_id INTEGER UNIQUE,
  proximity_id INTEGER UNIQUE,
  temperature_id INTEGER UNIQUE,
  movement_id INTEGER UNIQUE
);

drop table if exists message_log;
create table message_log(
  id INTEGER PRIMARY KEY,
  worker_id INTEGER,
  timestamp DATETIME,
  sentiment REAL
);

drop table if exists temperature_log;
create table temperature_log(
  id INTEGER PRIMARY KEY,
  worker_id INTEGER,
  timestamp DATETIME,
  temperature REAL
);

drop table if exists button_log;
create table button_log(
  id INTEGER PRIMARY KEY,
  worker_id INTEGER,
  timestamp DATETIME,
  button INTEGER
);

drop table if exists proximity_log;
create table proximity_log(
  id INTEGER PRIMARY KEY,
  worker_id INTEGER,
  timestamp DATETIME,
  proximity REAL
);

drop table if exists movement_log;
create table movement_log(
  id INTEGER PRIMARY KEY,
  worker_id INTEGER,
  timestamp DATETIME,
  proximity INTEGER
);"""
