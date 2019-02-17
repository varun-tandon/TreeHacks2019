from flask import Flask, render_template, url_for, request
import json
import os, sys
import random
import hashlib, uuid
import requests
import sendgrid
import plotly
import twitter
import pprint
import requests
import plotly.plotly as py
import plotly.graph_objs as go
from twilio.rest import Client
from .src.entities.entity import Session, engine, Base
from .src.entities.user import User
from sqlalchemy import and_
from sendgrid.helpers.mail import *

Base.metadata.create_all(engine)

#start session
session = Session()
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/onboarding')
def onboard():
    return render_template('intro_slides.html')

@app.route('/homepage')
def bill_card_page():
    return render_template('homepage.html')

@app.route('/verify_code_page')
def verify_code_page():
    return render_template('verify_code_page.html')

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
    response = dict()
    if(session.query(User).filter(and_(User.email == request_json['email'], User.password == hashed_password)).count() == 1):
        response['status'] = 200
        response['pass_key'] = hashed_password
        return json.dumps(response)
    else:
        response['status'] = 400
        return json.dumps(response)

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
        'x-api-key': "***REMOVED***",
        'Content-Type': "application/x-www-form-urlencoded",
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return str(response.json())

@app.route('/access_us_congress_info', methods=['POST'])
def get_us_congress_access():
    url = "https://q4ktfaysw3.execute-api.us-east-1.amazonaws.com/treehacks/legislators"
    content = request.get_json()

    querystring = {"address": content['zipcode'], "level": "NATIONAL_LOWER"}

    headers = {
        'x-api-key': "***REMOVED***",
        'Content-Type': "application/x-www-form-urlencoded",
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return str(response.json())

@app.route('/fax', methods=['POST'])
def fax_reps():
    account_sid = 'ACfc69560af65a93d8613594563ee29ce0'
    auth_token = 'abbe8c629b1dc6195541f75ad39e209c'
    client = Client(account_sid, auth_token)
    content = request.get_json()
    fax_number = content['fax_1']
    fax = client.fax.faxes \
        .create(
             from_='+15618011480',
             to= fax_number,
             media_url='http://edgepdf.rasteredge.com/RasterEdge_Cache/base/a3214e5f7d36406127741c22f7a98079/input/Fax%20Letter%20to%20Senators.pdf'
         )

    return fax_number

@app.route('/access_governor_info', methods=['GET'])
def get_governor_access():
    url = "https://q4ktfaysw3.execute-api.us-east-1.amazonaws.com/treehacks/legislators"
    content = request.get_json()

    querystring = {"address": content['zipcode'], "level": "STATE_EXEC"}

    headers = {
        'x-api-key': "***REMOVED***",
        'Content-Type': "application/x-www-form-urlencoded",
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return str(response.json())

@app.route('/send_sms_to_user', methods=['POST'])
def send_sms_to_user():
    url = "https://api.authy.com/protected/json/phones/verification/start"
    content = request.get_json()
    phone_number = content["phone_number"]
    payload = "api_key=***REMOVED***&via=sms&phone_number=" + phone_number + "&country_code=1&undefined="
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'Postman-Token': "b6895b26-2acb-40bd-9e35-60fc2d1634a8"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    result = dict()
    if(response.json()['success']):
        result['status'] = 200
    else:
        result['status'] = 400
    return json.dumps(result)

@app.route('/verify_user', methods=['POST'])
def get_verification():
    url = "https://api.authy.com/protected/json/phones/verification/check"
    content = request.get_json()
    phone_number = content["phone_number"]
    verification_code = content["verification_code"]
    url = "https://api.authy.com/protected/json/phones/verification/check"
    querystring = {"api_key":"***REMOVED***","verification_code": verification_code,"phone_number": phone_number,"country_code":"1"}

    payload = ""
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'Postman-Token': "3f68ad36-0caf-4713-860f-27f145fe85b8"
        }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    result = dict()
    if(response.json()['success']):
        result['status'] = 200
    else:
        result['status'] = 400
    return json.dumps(result)

@app.route('/azure_text_sentiment', methods=['POST'])
def azure_text_sentiment():
    url = "https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment"
    content = request.get_json()
    text = content['text']
    payload = " {\n        \"documents\": [\n            {\n                \"language\": \"en\",\n                \"id\": \"1\",\n                \"text\": \""+ text +"\"  \n}\n        ]\n    }"

    headers = {
        'Ocp-Apim-Subscription-Key': "***REMOVED***",
        'Content-Type': "application/json",
        'Accept': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "ee259beb-4450-4d89-9023-0fded2a3998e"
        }


    response = requests.request("POST", url, data=payload, headers=headers)
    json_response = json.dumps(response.text)
    text_score = json_response[41:59]
    # score = float(text_score)
    # print(score)
    return text_score

@app.route('/send_email_to_rep', methods=['POST'])
def send_email_to_rep():
    sg = sendgrid.SendGridAPIClient(apikey='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')
    from_email = Email("yourconstiuents@insession.com")
    content = request.get_json()
    representative_email = content["representative_email"]
    representative_name = content["representative_name"]
    name = content["constituent_name"]
    text = content["email_content"]
    to_email = Email(representative_email)
    subject = "I'm voicing my opinion"
    content = Content("text/plain", "Dear " + representative_name + ",  " + text + "\n""From, ""\n" + name)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)

    return name

@app.route('/get_zip_code', methods=['GET'])
def get_user_zipcode():
    user = session.query(User).filter(session.query(User).filter(and_(User.email == request_json['email'], User.password == request_json['access_token']))).one()
    return user.zipcode

@app.route('/twitter_scrape_machine', methods=['POST'])
def twitter_scrape_data_graph():
    api = twitter.Api(consumer_key='***REMOVED***',
                          consumer_secret='***REMOVED***',
                          access_token_key='***REMOVED***',
                          access_token_secret='***REMOVED***')
    results = api.GetSearch(
        raw_query="q=Kamala Harris%20&result_type=recent&since=2014-07-19&count=100")

    url = "https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment"
    total_amt = 0
    num_processed = 0
    num_pos = 0
    num_neut = 0
    num_neg = 0
    for i in range(100):
        print(i)
        text = str(results[i].text.encode('ascii', errors='ignore'))
        payload = "\n{\n\t\"documents\": [{\n\t\t\"language\": \"en\",\n\t\t\"id\": \"1\",\n\t\t\"text\": \"" + text + "\"\n\t}\n}"
        headers = {
            'Ocp-Apim-Subscription-Key': "***REMOVED***",
            'Content-Type': "application/json",
            'Accept': "application/json",
            'cache-control': "no-cache",
            'Postman-Token': "ee259beb-4450-4d89-9023-0fded2a3998e"
            }

        try:
            response = requests.request("POST", url, data=payload, headers=headers)
            sent = (response.json()['documents'][0]['score'])
            total_amt += sent
            if(sent > 0.6):
                num_pos += 1
            elif(sent < 0.4):
                num_neg += 1
            else:
                num_neut += 1
            num_processed += 1
        except:
            i -= 1
    print(total_amt / num_processed)
    print(num_pos)
    print(num_neut)
    print(num_neg)
        # text_score = json.dumps(response.text)
        # score = float(text_score)
        # print(score)


    labels = ['Positive','Neutral','Negative']
    values = [num_pos, num_neut, num_neg]
    colors = ['#00FF00', '#FFFF00', '#FF0000']

    trace = go.Pie(labels=labels, values=values,
                   hoverinfo='label+percent', textinfo='value',
                   textfont=dict(size=20),
                   marker=dict(colors=colors,
                               line=dict(color='#000000', width=2)))

    py.plot([trace], filename='Senator Harris Opinion Twitter Database')
