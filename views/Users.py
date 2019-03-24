from flask import current_app
from flask_restful import Resource

from database.definition import db
from database.models import User


class Users(Resource):
    def __init__(self):
        self.logger = current_app.logger
        self.logger.info("Initializing User instance")

    def __del__(self):
        self.logger.error("Destroying  User instance")

    def get(self):
        users = User.query.first()
        import pdb
        pdb.set_trace()
        return {'users': users}, 200

    def post(self):
        data = {
            'first_name': 'Samson',
            'last_name': 'Rapando',
            'gender': 'M'
        }
        new_user = User(**data)
        db.session.add(new_user)
        db.session.commit()
        return data, 200
