import requests

def get_Verification():

    url = "https://api.authy.com/protected/json/phones/verification/check"

    querystring = {"api_key":"stO4POVY4AJv5ucsr3O3oPbfk92p2R6i","verification_code": verification_code,"phone_number": phone_number,"country_code":"1"}

    payload = ""
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'Postman-Token': "3f68ad36-0caf-4713-860f-27f145fe85b8"
        }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    return response.text
