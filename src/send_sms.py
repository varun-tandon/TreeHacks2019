import requests

url = "https://api.authy.com/protected/json/phones/verification/start"

querystring = {"api_key":"***REMOVED***","via":"sms","phone_number":"5618011480","country_code":"1"}

payload = ""
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'Postman-Token': "77dff502-beb4-4b70-85d7-b091ff3880af"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)
