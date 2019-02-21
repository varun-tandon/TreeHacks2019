import requests
from flask import Flask, render_template, url_for, request

def azure_text_sentiment():
    url = "https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment"
    content = request.get_json()

    payload = " {\n        \"documents\": [\n            {\n                \"language\": \"en\",\n                \"id\": \"1\",\n                \"text\": \"I totally agree with this bill. I think that you should vote it through because it is essential to our environment.\"\n            },\n            {\n                \"language\": \"en\",\n                \"id\": \"2\",\n                \"text\": \"I think this bill is terrible. If you vote yes, I will not vote for you again.\"\n            },\n            {\n                \"language\": \"en\",\n                \"id\": \"3\",\n                \"text\": \"Everyone in my family liked the trail but thought it was too challenging for the less athletic among us. Not necessarily recommended for small children.\"\n            },\n            {\n                \"language\": \"en\",\n                \"id\": \"4\",\n                \"text\": \"It was foggy so we missed the spectacular views, but the trail was ok. Worth checking out if you are in the area.\"\n            },                \n            {\n                \"language\": \"en\",\n                \"id\": \"5\",\n                \"text\": \"This is my favorite trail. It has beautiful views and many places to stop and rest\"\n            }\n        ]\n    }"

    headers = {
        'Ocp-Apim-Subscription-Key': "",
        'Content-Type': "application/json",
        'Accept': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "ee259beb-4450-4d89-9023-0fded2a3998e"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    return response.text
