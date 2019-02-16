import requests

def get_Verification():
    url = "https://api.authy.com/protected/json/phones/verification/check"
    phone number = #figure out later
    verification_code = #figure out later
    payload = "api_key=tzsvpYNDQSEsQqFnYT5sNeCWNLXs7Qum&verification_code=" + verification_code + "&phone_number=" + phone_number + "&country_code=1&undefined="
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'Postman-Token': "82c404e3-6e66-4a4b-ae14-0ea702ce44c8"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
