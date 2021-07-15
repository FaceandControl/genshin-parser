from flask import make_response
from flask_restful import Resource
import json
from src import db
from src.models import Characters

class Сharacters(Resource):
    def get(self, ln):
        if ln == "en":
            curr_character = Characters.query.filter(Characters.eng_endpoint.startswith("en")).all()
            char_dict = {}
            for i in curr_character:
                char_dict[i.eng_name] = i.eng_endpoint
        else:
            curr_character = Characters.query.filter(Characters.ru_endpoint.startswith("ru")).all()
            char_dict = {}
            for i in curr_character:
                char_dict[i.ru_name] = i.ru_endpoint
        f_json = json.dumps(char_dict, ensure_ascii=False, indent=4)
        return make_response(f_json,200)