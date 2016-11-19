import os
import sqlite3
from flask import Flask, g, jsonify, request

#APP_CONFIG
app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'workit.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='admin'
))

#CONSTANTS
token = "COMMAND TOKENS TO VERIFY ONCE IT'S CREATED"

#DB_UTILS
def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

#API_FUNCTIONS
@app.route('/')
def hello_world():
    return 'Flask Dockerized'

@app.route('/test', methods=['POST'])
def test_commands():
    r = jsonify(request.form)

    response = jsonify({
        "response_type": "ephemeral",
        "text": "This functionality works well!"
    })

    #"HTTP/1.1 200 OK\r\nContent-type: application/json\r\n\r\n" + response

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')
