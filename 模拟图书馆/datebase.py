#__*__ encoding:utf-8 __*__
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db=SQLAlchemy(app)
class Book(db.Model):
    __tablename__ = 'BOOKS'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    author=db.Column(db.String(20),nullable=False)
    btype=db.Column(db.String(20),nullable=True)
    num = db.Column(db.Integer, nullable=False)
db.create_all()
