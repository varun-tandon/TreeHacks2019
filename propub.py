import json
import requests



url = "https://api.propublica.org/congress/v1/115/house/bills/introduced.json"

#querystring = {"summary_short"}

headers = {
    'X-API-Key': 'DthNpqjA4QjYSXHy65GqeHHHcnFznlZV5qh2LOLI',
}


#gives you the bills as a dictionary
def getBills():
    response = requests.get(url, headers=headers)
    content = response.json()
    content1 = content["results"][0]["bills"]#[2]["summary_short"]
    i = 0
    bills = {}
    while i < len(content1):
        print(content1[i]["sponsor_name"])
        print(content1[i]["summary_short"])
        bills[content1[i]["sponsor_name"]] = content1[i]["summary_short"]
        i += 1
    print(bills)
    return bills

#returns a specific bill as a string
def getBillSummary(id, congressNum):
    url = "https://api.propublica.org/congress/v1/" + congressNum + "/bills/" + id + ".json"
    response = requests.get(url, headers=headers)
    content = response.json()
    billData = {}
    #print(content)
    #print(content["results"][0]["title"])
    billData[content["results"][0]["title"]] = content["results"][0]["summary"]
    return billData

#returns most recent bills
def getRecentBills():
    url = "https://api.propublica.org/congress/v1/115/house/bills/introduced.json"
    response = requests.get(url, headers=headers)
    content = response.json()
    #print(content)
    contentList = content["results"][0]["bills"]
    billRecents = {}
    i = 0
    while i < len(contentList):
        #print(contentList[i]["title"])
        #print(contentList[i]["summary"])
        billRecents[contentList[i]["title"]] = contentList[i]["summary"]
        i += 1
    return billRecents

getRecentBills()
