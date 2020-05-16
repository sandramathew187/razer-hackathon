from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import requests
import json 
import sys
import random

headers = {  'Accept': 'application/vnd.mambu.v2+json'}
r = requests.get('https://localhost:8889/api/loans/{loanAccountId}', params={}, headers = headers)
print (r.json())

# Make app into flask
app = Flask(__name__)

# Tell program where database is
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/SME'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class SME(db.Model):
    __tablename__ = 'SME'

    loanID = db.Column(db.Integer, nullable = True)
    cName = db.Column(db.String(50), nullable=False)
    CID = db.Column(db.Integer, primary_key=True)
    employees = db.Column(db.Integer, nullable=False)
    revenue = db.Column(db.String(50), nullable=False)  #float
    assets = db.Column(db.Integer, nullable=False)      #float
    industry = db.Column(db.String(50), nullable=False)
    
    def __init__(self, loanID, cName, CID, employees, revenue, assets, industry, number): 
        self.loanID = loanID
        self.cName = cName
        self.CID = CID
        self.employees = employees
        self.revenue = revenue
        self.assets = assets
        self.industry = industry

    def json(self):
        return {"loanID": self.loanID, 
                "cName": self.cName, 
                "CID": self.CID, 
                "employees": self.employees, 
                "revenue": self.revenue,
                "assets": self.assets,
                "industry": self.industry}

#create loanID in LOAN table
@app.route("/loan/<string:cName>", methods=['POST'])
def create_loan_account(cName):
    try:
        stmt = SME.query.filter_by(cName=cName).first()
        loanID = stmt.loanID
        if loanID == None:
            loanID = random.randrange(10000, 99999) 
            stmt.loanID = loanID
            db.session.commit()
            return jsonify({"message": "Loan account successfully created"}), 201
        else:
            return jsonify({"message": "A loan account with loanID '{}' already exists.".format(loanID)}), 400 
    
    except:
        return jsonify({"message" : "Company Name '{}' does not exist.".format(cName)}), 400


headers = {'Content-type': 'application/json'}
r = requests.get('https://razerhackathon.sandbox.mambu.com/api/loans/{{loanAccount}}/transactions', params={}, headers = headers)

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port=5700, debug=True)
