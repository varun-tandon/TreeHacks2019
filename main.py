from flask import Flask, render_template, url_for, request
import json
import os, sys
import random
import hashlib, uuid
import requests
from .src.entities.entity import Session, engine, Base
from .src.entities.user import User
from sqlalchemy import and_

Base.metadata.create_all(engine)

#start session
session = Session()
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/create_user', methods=['POST'])
def create_user():
    request_json = request.get_json()
    hashed_password = hashlib.sha512(request_json['password'].encode('utf-8')).hexdigest()
    if(session.query(User).filter(User.email == request_json['email']).count() == 0):
        new_user = User(request_json['email'], hashed_password)
        session.add(new_user)
        session.commit()
        return "completed"
    return "user already exists"

@app.route('/login', methods=['POST'])
def login_user():
    request_json = request.get_json()
    hashed_password = hashlib.sha512(request_json['password'].encode('utf-8')).hexdigest()
    if(session.query(User).filter(and_(User.email == request_json['email'], User.password == hashed_password)).count() == 1):
        return "SUCCESS"
    return "0 or more users"

# NATIONAL_EXEC : Refers to the President, VP, etc
# NATIONAL_UPPER : Refers to U.S. Senate members
# NATIONAL_LOWER : Refers to U.S. Congress members
# STATE_EXEC : Refers to state governors
# STATE_UPPER : Refers to state senators
# STATE_LOWER : Refers to state congress members


@app.route('/access_us_senators_info', methods=['GET'])
def get_us_senators_access():
    url = "https://q4ktfaysw3.execute-api.us-east-1.amazonaws.com/treehacks/legislators"
    content = request.get_json()

    querystring = {"address": content['zipcode'], "level": "NATIONAL_UPPER"}

    headers = {
        'x-api-key': "2e1uvo7yeX50ZGHvctPxi8ZWubhggyOydIWvOa5c",
        'Content-Type': "application/x-www-form-urlencoded",
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text

@app.route('/access_us_congress_info', methods=['GET'])
def get_us_congress_access():
    url = "https://q4ktfaysw3.execute-api.us-east-1.amazonaws.com/treehacks/legislators"
    content = request.get_json()

    querystring = {"address": content['zipcode'], "level": "NATIONAL_LOWER"}

    headers = {
        'x-api-key': "2e1uvo7yeX50ZGHvctPxi8ZWubhggyOydIWvOa5c",
        'Content-Type': "application/x-www-form-urlencoded",
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text

@app.route('/access_governor_info', methods=['GET'])
def get_governor_access():
    url = "https://q4ktfaysw3.execute-api.us-east-1.amazonaws.com/treehacks/legislators"
    content = request.get_json()

    querystring = {"address": content['zipcode'], "level": "STATE_EXEC"}

    headers = {
        'x-api-key': "2e1uvo7yeX50ZGHvctPxi8ZWubhggyOydIWvOa5c",
        'Content-Type': "application/x-www-form-urlencoded",
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text
