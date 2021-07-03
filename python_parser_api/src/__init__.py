from flask import Flask
from flask_restful import Api
from logging import FileHandler, WARNING

app = Flask(__name__)

api = Api(app)

#logging customization
file_error_handler = FileHandler('logs/errorlog.txt')
file_error_handler.setLevel(WARNING)
app.logger.addHandler(file_error_handler)
