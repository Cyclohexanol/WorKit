import os
import sqlite3
from oauth2_config import oauth2_config
from flask import Flask, g, jsonify, request, redirect


#APP_CONFIG
app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'workit.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='admin'
))

#Dynamically setting the PORT
port = int(os.getenv('PORT', '5000'))

#CONSTANTS
token = "MP6bV33AHeBEFxDdUBjaoBsG"
config = oauth2_config((["users:read", "channels:history", "channels:read", "channels:write", "chat:write:bot",
"incoming-webhook", "commands", "bot"]), "107526814087.107515751334", "b8b2779318baa62d6e71dd9e2f07e247", "https://workit-py.scapp.io/authenticate")

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
    test_token = r['token']

    if token == test_token:

        response = jsonify({
            "status": "200",
            "response_type": "ephemeral",
            "text": "This functionality works well!"
        })

        return response
    else:
        return jsonify({
            "status": "failed"
        })

@app.route('/autorise', methods=['GET'])
def autorisation():
    separator = " "

    url = ("https://slack.com/oauth/authorize?" +
        "client_id=" + config.client_id +
        "&scope=" + separator.join(config.scopes) +
        "&redirect_uri=" + config.redirect_uri)

    return redirect(url)

@app.route('/authenticate', methods=['GET'])
def authentication():
    separator = " "

    url = ("https://slack.com/api/oauth.access?" +
        "client_id=" + config.client_id +
        "&client_secret=" + config.client_secret +
        "&code=" + request.args['code'] +
        "&redirect_uri=" + config.redirect_uri)

    return redirect(url)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
