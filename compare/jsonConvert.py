#RUN ONCE PER PATCH TO GENERATE DICTIONARY OF DBFID: REST OF CARD DATA

import requests
import json

url = 'https://api.hearthstonejson.com/v1/31022/enUS/cards.collectible.json'

json_data = requests.get(url).json()

tidyDict = {}

def build():
    for i in json_data:
        dbfId = i['dbfId']
        card = i

        tidyDict[dbfId]=i


#print(json_data)
build()

with open('../cardData', 'w') as f:
    json.dump(tidyDict, f)
