"""drop table if exists workers;
create table workers(
  id INTEGER NOT NULL PRIMARY KEY,
  team_name varchar(64) NOT NULL,
  button_id varchar(64) UNIQUE,
  proximity_id varchar(64) UNIQUE,
  temperature_id varchar(64) UNIQUE,
  movement_id varchar(64) UNIQUE
);

drop table if exists gateways:
create table gateways(
  id varchar(64) NOT NULL PRIMARY KEY,
  building varchar(32)
);

drop table if exists message_log;
create table message_log(
  id INTEGER NOT NULL PRIMARY KEY,
  worker_id INTEGER NOT NULL FOREIGN KEY REFERENCES workers(id),
  timestamp DATETIME,
  sentiment REAL
);

drop table if exists temperature_log;
create table temperature_log(
  id INTEGER NOT NULL PRIMARY KEY,
  worker_id INTEGER NOT NULL FOREIGN KEY REFERENCES workers(id),
  timestamp DATETIME,
  temperature REAL
);

drop table if exists button_log;
create table button_log(
  id INTEGER NOT NULL PRIMARY KEY,
  worker_id INTEGER NOT NULL FOREIGN KEY REFERENCES workers(id),
  timestamp DATETIME
);

drop table if exists proximity_log;
create table proximity_log(
  id INTEGER NOT NULL PRIMARY KEY,
  worker_id INTEGER NOT NULL FOREIGN KEY REFERENCES workers(id),
  timestamp DATETIME,
  gateway_id varchar(64) NOT NULL FOREIGN KEY REFERENCES gateways(id)
);

drop table if exists movement_log;
create table movement_log(
  id INTEGER NOT NULL PRIMARY KEY,
  worker_id INTEGER NOT NULL FOREIGN KEY REFERENCES workers(id),
  timestamp DATETIME,
  movement INTEGER
);"""
