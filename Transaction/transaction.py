from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
from random import randrange
from datetime import datetime
import sys
import requests
import json


app = Flask(__name__, template_folder='../templates')
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/booking'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)


class transaction(db.Model):
    __tablename__ = 'transaction'

    companyname = db.Column(db.integer(), primary_key=True)
    percentagerevenue = db.Column(db.string(128), nullable=False)

    def __init__(self, companyname, percentagerevenue):
        self.companyname = companyname
        self.percentagerevenue = percentagerevenue

    def json(self):
        return {'Company Name': self.companyname, 'Percentage Revenue': self.percentagerevenue}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)