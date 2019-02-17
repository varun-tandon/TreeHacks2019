import json

import requests



url = "https://api.propublica.org/congress/v1/115/house/bills/introduced.json"

#querystring = {"summary_short"}

headers = {
    'X-API-Key': 'DthNpqjA4QjYSXHy65GqeHHHcnFznlZV5qh2LOLI',
}

response = requests.get(url, headers=headers)
content = response.json()
content1 = content["results"][0]["bills"]#[2]["summary_short"]

i = 0
while i < len(content1):
    print(content1[i]["sponsor_name"])
    print(content1[i]["summary_short"])
    i += 1


url1 = "https://api.propublica.org/congress/v1/105-115/both/bills/introduced_2/16/19.json"

print("new")

#querystring = {"summary_short"}

headers = {
    'X-API-Key': 'DthNpqjA4QjYSXHy65GqeHHHcnFznlZV5qh2LOLI',
}

response = requests.get(url1, headers=headers)
content = response.json()
content1 = content["results"][0]["bills"]#[2]["summary_short"]

i = 0
while i < len(content1):
    print(content1[i]["sponsor_name"])
    print(content1[i]["summary_short"])
    i += 1
GET
