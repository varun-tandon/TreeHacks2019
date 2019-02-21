from flask import requests
import requests
import json

@app.route('/access_rep_info', methods=['GET'])
def get_rep_access()
    url = "https://q4ktfaysw3.execute-api.us-east-1.amazonaws.com/treehacks/legislators"
    querystring = {"address": json.loads(requests.get_json())['zipcode']}

    headers = {
        'x-api-key': "",
        'Content-Type': "application/x-www-form-urlencoded",
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


# NATIONAL_EXEC : Refers to the President, VP, etc
# NATIONAL_UPPER : Refers to U.S. Senate members
# NATIONAL_LOWER : Refers to U.S. Congress members
# STATE_EXEC : Refers to state governors
# STATE_UPPER : Refers to state senators
# STATE_LOWER : Refers to state congress members
