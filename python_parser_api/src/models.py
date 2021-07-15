from src import db

class Characters(db.Model):

    __tablename__ = 'characters'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    eng_name = db.Column(db.String(30),nullable=False, unique=True)
    eng_link = db.Column(db.String(200),nullable=False, unique=True)
    eng_endpoint = db.Column(db.String(30),nullable=False, unique=True)
    ru_name = db.Column(db.String(30),nullable=False, unique=True)
    ru_link = db.Column(db.String(200),nullable=False, unique=True)
    ru_endpoint = db.Column(db.String(30),nullable=False, unique=True)