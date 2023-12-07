from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    username = db.Column(db.String(50),primary_key = True)
    password = db.Column(db.String(50), nullable = False)
    score = db.Column(db.Integer)