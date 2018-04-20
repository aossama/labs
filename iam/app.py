import os
import sys
import json
import argparse

from flask import Flask, request, jsonify, current_app
from flask_restful import Resource, Api
from sqlalchemy.orm.exc import NoResultFound
from flask_cors import CORS

from utils.sa import Database, User


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)


app = Flask(__name__)

app.config.from_object('conf.base')
app.config.from_envvar('ENV_SETTINGS')

cors = CORS(app, resources={
    r"/1/signup/": {"origins": "*"},
    r"/1/verify_auth/": {"origins": "*"}
})
api = Api(app)


class BaseAPI(Resource):
    def __init__(self):
        print("Create new database")
        Database().setup()
        db = Database()
        self.session = db.get_session()


class Home(BaseAPI):
    """ Serve the API version information"""

    @staticmethod
    def get():
        return "Labs IAM API v0.1"


class Users(BaseAPI):
    def post(self):
        json_data = request.get_json(force=True)
        username = json_data['username']
        password = json_data['password']

        try:
            self.session.query(User).filter(User.username == username).one()
            return jsonify(result="Username is already taken!")
        except NoResultFound:
            u = User(username=username, password=password)
            u.save(self.session)

            # r = redis.StrictRedis(host='172.17.0.2', port=6379, db=0)
            # message = {"username": username, "password": password}
            # r.publish('iam-to-auth', json.dumps(message).encode('utf-8'))

            return jsonify(result="User created")


class VerifyAuth(BaseAPI):
    def post(self):
        json_data = request.get_json(force=True)
        username = json_data['username']
        password = json_data['password']

        try:
            user = self.session.query(User).filter(
                User.username == username,
                User.password == password).one()
            paylod = {'username': user.username, 'id': user.id}
            return jsonify(result=200, user=json.dumps(paylod))
        except NoResultFound:
            return jsonify(result=404)


api.add_resource(Home, '/1/')
api.add_resource(Users, '/1/signup/')
api.add_resource(VerifyAuth, '/1/verify_auth/')


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
