#NOT USED
#example searching through json dictionary

import requests

url = 'https://api.hearthstonejson.com/v1/31022/enUS/cards.collectible.json'

json_data = requests.get(url).json()

def search(dbfId):
    for i in json_data:
        if i['dbfId'] == dbfId:
            return i['name']

print(search(397))

#print(json_data)
