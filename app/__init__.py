from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_restful import Api
from flask_migrate import Migrate
from flask_cors import CORS
app = Flask(__name__)
api = Api(app)
CORS(app)
app.config.from_object(Config)
app.config['BUNDLE_ERRORS'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes,  models

