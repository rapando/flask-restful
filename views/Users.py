from flask_restful import Resource
from flask import current_app
from database.models import User


class Users(Resource):
    def __init__(self):
        self.logger = current_app.logger
        self.logger.info("Initializing User instance")

    def __del__(self):
        self.logger.error("Destroying  User instance")

    def get(self):
        users = User.query.all()
        return {'users': users}, 200
