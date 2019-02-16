from flask import Flask, render_template, url_for, request
import json
import pandas as pd
import os
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')
