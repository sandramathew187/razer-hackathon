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
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/sponsor'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)


class Sponsor(db.Model):
    __tablename__ = 'Sponsor'

    companyname = db.Column(db.String(128), nullable=False)
    companyid = db.Column(db.Integer, nullable=False)
    depositid = db.Column(db.String(128), primary_key=True)
    percentagerevenue = db.Column(db.Integer, nullable=False)

    def __init__(self, companyname, companyid, depositid, percentagerevenue):
        self.companyname = companyname
        self.companyid = companyid
        self.depositid = depositid
        self.percentagerevenue = percentagerevenue

    def json(self):
        return {'companyname': self.companyname, 'companyid': self.companyid, 'depositid': self.depositid, 'percentagerevenue': self.percentagerevenue}

@app.route('/sponsor/new', methods=["POST"])
def signupassponsor():
    data = request.get_json()
    sponsor = Sponsor(data["companyname"], data["depositid"], data["companyid"], data["percentagerevenue"])

    try:
        db.session.add(sponsor)
        db.session.commit()
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return jsonify({"message": "An error occurred."}), 500

    return jsonify(sponsor.json()), 201 

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)