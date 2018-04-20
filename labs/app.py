import os
import sys
import argparse

from flask import Flask, current_app
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required, current_identity, JWTError
from flask_cors import CORS

from utils.sa import Database, Lab


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)


def authenticate():
    return None


def identity(payload):
    user_identity = payload['identity']
    return user_identity


app = Flask(__name__)

app.config.from_object('conf.base')
app.config.from_envvar('ENV_SETTINGS')

jwt = JWT(app, authenticate, identity)
cors = CORS(app, resources={r"*": {"origins": "*"}})
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
    @jwt_required()
    def get():
        return "Labs API v0.1"


class WhoAmI(BaseAPI):
    @jwt_required()
    def get(self):
        return '%s' % current_identity


class Catalog(BaseAPI):
    @jwt_required()
    def get(self):
        labs = self.session.query(Lab).all()

        if len(labs) > 0:
            for lab in self.session.query(labs):
                print(lab.name)
        else:
            return "No labs found"


class Labs(BaseAPI):
    """ Serve the base for Lab Endpoint"""

    @staticmethod
    @jwt_required()
    def get(lab_id):
        return "Viewing lab {}".format(lab_id)

    @staticmethod
    @jwt_required()
    def post(lab_id):
        return "Enrolling in lab {}".format(lab_id)

    @jwt_required()
    def delete(self):
        return "Disable Lab"


api.add_resource(Home, '/1/')
api.add_resource(WhoAmI, '/1/whoami', endpoint='whoami')
api.add_resource(Catalog, '/1/catalog/', endpoint='get_catalog')
api.add_resource(Labs, '/1/lab/<int:lab_id>', endpoint='get_lab_id')


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
