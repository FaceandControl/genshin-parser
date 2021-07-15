from flask import make_response
from flask_restful import Resource
from bs4 import BeautifulSoup
import requests
import json
import re
from src import db
from src.models import Characters

# name_to_link_ru = {
#     "albedo":"https://genshin-impact.fandom.com/ru/wiki/%D0%90%D0%BB%D1%8C%D0%B1%D0%B5%D0%B4%D0%BE",
#     "barbara":"https://genshin-impact.fandom.com/ru/wiki/%D0%91%D0%B0%D1%80%D0%B1%D0%B0%D1%80%D0%B0",
#     "bennett":"https://genshin-impact.fandom.com/ru/wiki/%D0%91%D0%B5%D0%BD%D0%BD%D0%B5%D1%82",
#     "beidou":"https://genshin-impact.fandom.com/ru/wiki/%D0%91%D1%8D%D0%B9_%D0%94%D0%BE%D1%83",
#     "venti":"https://genshin-impact.fandom.com/ru/wiki/%D0%92%D0%B5%D0%BD%D1%82%D0%B8",
#     "ganyu":"https://genshin-impact.fandom.com/ru/wiki/%D0%93%D0%B0%D0%BD%D1%8C_%D0%AE%D0%B9",
#     "jean":"https://genshin-impact.fandom.com/ru/wiki/%D0%94%D0%B6%D0%B8%D0%BD%D0%BD",
#     "diluc":"https://genshin-impact.fandom.com/ru/wiki/%D0%94%D0%B8%D0%BB%D1%8E%D0%BA",
#     "diona":"https://genshin-impact.fandom.com/ru/wiki/%D0%94%D0%B8%D0%BE%D0%BD%D0%B0",
#     "kazuha":"https://genshin-impact.fandom.com/ru/wiki/%D0%9A%D0%B0%D0%B4%D0%B7%D1%83%D1%85%D0%B0",
#     "klee":"https://genshin-impact.fandom.com/ru/wiki/%D0%9A%D0%BB%D0%B8",
#     "keqing":"https://genshin-impact.fandom.com/ru/wiki/%D0%9A%D1%8D_%D0%A6%D0%B8%D0%BD",
#     "kaeya":"https://genshin-impact.fandom.com/ru/wiki/%D0%9A%D1%8D%D0%B9%D0%B0",
#     "lisa":"https://genshin-impact.fandom.com/ru/wiki/%D0%9B%D0%B8%D0%B7%D0%B0",
#     "mona":"https://genshin-impact.fandom.com/ru/wiki/%D0%9C%D0%BE%D0%BD%D0%B0",
#     "ningguang":"https://genshin-impact.fandom.com/ru/wiki/%D0%9D%D0%B8%D0%BD_%D0%93%D1%83%D0%B0%D0%BD",
#     "noelle":"https://genshin-impact.fandom.com/ru/wiki/%D0%9D%D0%BE%D1%8D%D0%BB%D0%BB%D1%8C",
#     "traveler":"https://genshin-impact.fandom.com/ru/wiki/%D0%9F%D1%83%D1%82%D0%B5%D1%88%D0%B5%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%B8%D0%BA",
#     "rosaria":"https://genshin-impact.fandom.com/ru/wiki/%D0%A0%D0%BE%D0%B7%D0%B0%D1%80%D0%B8%D1%8F",
#     "razor":"https://genshin-impact.fandom.com/ru/wiki/%D0%A0%D1%8D%D0%B9%D0%B7%D0%BE%D1%80",
#     "sucrose":"https://genshin-impact.fandom.com/ru/wiki/%D0%A1%D0%B0%D1%85%D0%B0%D1%80%D0%BE%D0%B7%D0%B0",
#     "xingqiu":"https://genshin-impact.fandom.com/ru/wiki/%D0%A1%D0%B8%D0%BD_%D0%A6%D1%8E",
#     "xinyan":"https://genshin-impact.fandom.com/ru/wiki/%D0%A1%D0%B8%D0%BD%D1%8C_%D0%AF%D0%BD%D1%8C",
#     "xiangling":"https://genshin-impact.fandom.com/ru/wiki/%D0%A1%D1%8F%D0%BD_%D0%9B%D0%B8%D0%BD",
#     "xiao":"https://genshin-impact.fandom.com/ru/wiki/%D0%A1%D1%8F%D0%BE",
#     "tartaglia":"https://genshin-impact.fandom.com/ru/wiki/%D0%A2%D0%B0%D1%80%D1%82%D0%B0%D0%BB%D1%8C%D1%8F",
#     "fischl":"https://genshin-impact.fandom.com/ru/wiki/%D0%A4%D0%B8%D1%88%D0%BB%D1%8C",
#     "hu_tao":"https://genshin-impact.fandom.com/ru/wiki/%D0%A5%D1%83_%D0%A2%D0%B0%D0%BE",
#     "qiqi":"https://genshin-impact.fandom.com/ru/wiki/%D0%A6%D0%B8_%D0%A6%D0%B8",
#     "zhongli":"https://genshin-impact.fandom.com/ru/wiki/%D0%A7%D0%B6%D1%83%D0%BD_%D0%9B%D0%B8",
#     "chongyun":"https://genshin-impact.fandom.com/ru/wiki/%D0%A7%D1%83%D0%BD_%D0%AE%D0%BD%D1%8C",
#     "amber":"https://genshin-impact.fandom.com/ru/wiki/%D0%AD%D0%BC%D0%B1%D0%B5%D1%80",
#     "eula":"https://genshin-impact.fandom.com/ru/wiki/%D0%AD%D0%BE%D0%BB%D0%B0",
#     "yanfei":"https://genshin-impact.fandom.com/ru/wiki/%D0%AF%D0%BD%D1%8C_%D0%A4%D1%8D%D0%B9",
# }


class Сharacter(Resource):
    def get(self,ln, name):
        if ln == "en":
            curr_character = db.session.query(Characters).filter_by(eng_endpoint = "{}/character/{}".format("en", name)).first()
            link = curr_character.eng_link
        else:
            curr_character = db.session.query(Characters).filter_by(ru_endpoint = "{}/character/{}".format("ru", name)).first()
            link = curr_character.ru_link

        if not name or not curr_character:
            return make_response({"status":"no character "+name},404)
        data = requests.get(link)
        soup = BeautifulSoup(data.text, features='html.parser')
        e_dict = {}

        e_dict["name"] = soup.find("h1", class_="page-header__title").text
        e_dict["quotes"] = soup.find("div", class_="mw-parser-output").dl.dd.text
        d_s = soup.find("div", class_="tabbertab").find_all("p")
        e_dict["description"] = d_s[1].text + d_s[2].text + d_s[3].text

        main_block = soup.find("div", class_="mw-parser-output")
        key = "wrong"
        for i in main_block:
            if i.name == "h3" or i.name == "h2":
                if i.span.get("id") == "Личность":
                    key = "personality"
                elif i.span.get("id") == "Внешность":
                    key = "appearance"
                elif i.span.get("id") == "Боевые_характеристики":
                    key = "combat_characteristics"
                elif i.span.get("id") == "История":
                    key = "history"
                else:
                    key = "wrong"
                    continue
                e_dict[key]=""
            else:
                if key == "wrong":
                    continue
                if i.name == "dl":
                    e_dict[key] += i.dd.i.text+" "
                elif i.name == "p":
                    e_dict[key] += i.text+" "

        for i in e_dict.keys():
            e_dict[i] = e_dict[i].replace('\n', ' ')
            e_dict[i] = re.sub('([A-Z.])', r'\1 ', e_dict[i])
        
        f_json = json.dumps(e_dict, ensure_ascii=False, indent=4)
        return make_response(f_json,200)