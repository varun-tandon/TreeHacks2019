import requests

url = "https://api.authy.com/protected/json/phones/verification/start"
phone_number = #figure this out later
payload = "api_key=tzsvpYNDQSEsQqFnYT5sNeCWNLXs7Qum&via=sms&phone_number=" + phone_number + "&country_code=1&undefined="
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'Postman-Token': "b6895b26-2acb-40bd-9e35-60fc2d1634a8"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
