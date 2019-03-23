import logging
import os
import pdb

from cloghandler import ConcurrentRotatingFileHandler
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from database.models import db
from flask_migrate import Migrate


from views.Users import Users

# Configure logging
cur_dir = os.path.dirname(os.path.realpath(__file__))
log_file = os.path.join(cur_dir, "logs", "usermgmt.log")
handler = ConcurrentRotatingFileHandler(log_file, "a", 10737418240, 1000)


formatter = logging.Formatter(
    '%(asctime)s] - %(name)s - %(levelname)s in %(module)s:%(lineno)d:%(funcName)-10s %(message)s')
handler.setFormatter(formatter)

app = Flask(__name__)
app.config.from_pyfile(os.path.join(cur_dir, "conf", "configs.py"))
CORS(app)
db.init_app(app)
migrate = Migrate(app, db)
app.logger.addHandler(handler)
app.logger.setLevel(logging.DEBUG)


# API urls
api = Api(app)
api.add_resource(Users, '/users')

if __name__ == "__main__":
    app.run()
