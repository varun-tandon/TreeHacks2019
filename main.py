from flask import Flask, render_template, url_for, request
import json
import os, sys
import random
import hashlib, uuid

from os.path import dirname
sys.path.append(dirname(__file__))

from .src.entities.entity import Session, engine, Base
from .src.entities.user import User

Base.metadata.create_all(engine)

# start session
session = Session()

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/create_user', methods=['POST'])
def create_user():
    request_json = request.get_json()
    session.add(new_user)
    session.commit()
    return "completed"
