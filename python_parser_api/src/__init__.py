from flask import Flask
from flask_restful import Api
import pathlib
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from logging import FileHandler, WARNING

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

#logging customization
# file_error_handler = FileHandler('logs/errorlog.txt')
# file_error_handler.setLevel(WARNING)
# app.logger.addHandler(file_error_handler)

from src import routes, models