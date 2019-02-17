import twitter
from main import azure_text_sentiment
import pprint
import requests
import json
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
