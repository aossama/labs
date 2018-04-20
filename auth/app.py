import os
import sys
import json
import argparse
import requests

from flask import Flask, current_app
from flask_jwt import JWT, jwt_required, current_identity
from flask_cors import CORS


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)


class User(object):
    def __init__(self, id, username):
        self.id = id
        self.username = username


def authenticate(username, password):
    url = current_app.config['IAM_URL']
    payload = {'username': username, 'password': password}

    r = requests.post(url, data=json.dumps(payload))
    res = r.json()

    if res['result'] == 200:
        user = json.loads(res['user'])
        user = User(user['id'], user['username'])

        return user


def identity(payload):
    uid = payload['identity']
    return uid


app = Flask(__name__)

app.config.from_object('conf.base')
app.config.from_envvar('ENV_SETTINGS')

with app.app_context():
    auth_origin = current_app.config['AUTH_ORIGIN']
    cors = CORS(app, resources={
        r"/auth": {"origins": auth_origin},
    })

    jwt = JWT(app, authentication_handler=authenticate, identity_handler=identity)


@app.route('/whoami')
@jwt_required()
def protected():
    return '%s' % current_identity


def run_app():
    with app.app_context():
        parser = argparse.ArgumentParser()
        parser.add_argument('-p', '--port', type=int, required=False)
        parser.add_argument('--host', '--host', type=str, required=False)

        args = parser.parse_args()
        if args.port is None:
            args.port = current_app.config['PORT']
        if args.host is None:
            args.host = '127.0.0.1'

    app.run(host=args.host, port=args.port)


if __name__ == '__main__':
    run_app()
    # app.run()
