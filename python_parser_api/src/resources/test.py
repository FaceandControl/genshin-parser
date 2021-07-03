from flask import make_response
from flask_restful import Resource

class Test(Resource):
    def get(self):
        return make_response({"status":"OK"},200)