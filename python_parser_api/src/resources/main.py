from flask import make_response
from flask_restful import Resource

class Main(Resource):
    def get(self):
        return make_response(
            {
                "/":"main",
                "/<ln>/character/<name>":"character",
                "/<ln>/characters":"characters",
                }
                ,200)