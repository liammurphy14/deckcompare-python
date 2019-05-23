import decoder, json

code1 = 'AAECAf0ECoqeA5aaA4OWA6+HA6iHA6aHA6CAA8XzAooHigEKwpkD05gD55UD zYkDw/gC7AfhB6sEyQNNAA=='
code2 = 'AAECAf0ECIqeA6CbA5aaA62HA6iHA6CAA77sAqsEC9OYA4OWA82JA5n/AsP4 AsXzAuwHywTJA4oBTQA='

[0, 1, 2, 1, 637, 10, 53002, 52502, 51971, 50095, 50088, 50086, 49184, 47557, 906, 138, 10, 52418, 52307, 51943, 50381, 48195, 1004, 993, 555, 457, 77, 0]


decoded1 = decoder.decode(code1)
decoded2 = decoder.decode(code2)

def getCards(decoded):
    lenSingles = decoded[5]
    lenDoubles = decoded[5+lenSingles+1]
    singles = decoded[6:6+lenSingles]
    firstDoublePos = 6 + lenSingles + 1
    doubles = decoded[firstDoublePos:firstDoublePos+lenDoubles]
    return [singles, doubles]

def checkDupe(deck,allCards):
    #helps listAll() to build a list without duplicates
    for j in [0,1]:
        for i in deck[j]:
            if i not in allCards:
                allCards.append(i)

def listAll(deck1, deck2):
    #returns a list containing one of each card in one or both decks
    allCards = []
    checkDupe(deck1,allCards)
    checkDupe(deck2,allCards)
    return allCards

deck1 = getCards(decoded1)
deck2 = getCards(decoded2)

cardList = listAll(deck1,deck2)

cases = {'2/0':[],'2/1':[],'2/2':[],'1/0':[],'1/1':[],'1/2':[],'0/0':[],'0/1':[],'0/2':[],}

for i in cardList:
    #sorts cards into a dictionary, depending how many copies in each deck
    if i in deck1[0]:
        if i in deck2[0]:
            cases['1/1'].append(i)
        elif i in deck2[1]:
            cases['1/2'].append(i)
        else:
            cases['1/0'].append(i)
    elif i in deck1[1]:
        if i in deck2[0]:
            cases['2/1'].append(i)
        elif i in deck2[1]:
            cases['2/2'].append(i)
        else:
            cases['2/0'].append(i)
    else:
        if i in deck2[0]:
            cases['0/1'].append(i)
        elif i in deck2[1]:
            cases['0/2'].append(i)
        else:
            cases['0/0'].append(i)

def printCard(n,dbfId):
    if n == 1:
        mult = '1x '
    elif n == 2:
        mult = '2x '

    cardName = cardList[str(dbfId)]['name']
    print(mult + cardName)

with open('cardlist', 'r') as f:
    cardList = json.load(f)

print('DECK COMPARISON RESULT:')
print('-----------------------')
print('Cards in Deck 1:')
for i in cases['2/0']:
    printCard(2,i)
for i in cases['2/1']:
    printCard(1,i)
for i in cases['1/0']:
    printCard(1,i)
print('-----------------------')
print('Cards in both decks:')
for i in cases['2/2']:
    printCard(2,i)
for i in cases['1/1']:
    printCard(1,i)
for i in cases['2/1']:
    printCard(1,i)
for i in cases['1/2']:
    printCard(1,i)
print('-----------------------')
print('Cards in Deck 2:')
for i in cases['0/2']:
    printCard(2,i)
for i in cases['1/2']:
    printCard(1,i)
for i in cases['0/1']:
    printCard(1,i)
print('-----------------------')
print('Cards in no decks (something went wrong if this is populated):')
for i in cases['0/0']:
    printCard(1,i)
