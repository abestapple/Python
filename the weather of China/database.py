#__*__ encoding:utf-8 __*__
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///city_code.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db=SQLAlchemy(app)
class Code(db.Model):
    __tablename__ = 'CODE'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    city = db.Column(db.String(20), nullable=False)
    code=db.Column(db.String(100),nullable=False)
db.create_all()
