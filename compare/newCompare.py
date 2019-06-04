import json
from .decoder import *

code1 = 'AAECAf0ECoqeA5aaA4OWA6+HA6iHA6aHA6CAA8XzAooHigEKwpkD05gD55UD zYkDw/gC7AfhB6sEyQNNAA=='
code2 = 'AAECAf0ECIqeA6CbA5aaA62HA6iHA6CAA77sAqsEC9OYA4OWA82JA5n/AsP4 AsXzAuwHywTJA4oBTQA='

[0, 1, 2, 1, 637, 10, 53002, 52502, 51971, 50095, 50088, 50086, 49184, 47557, 906, 138, 10, 52418, 52307, 51943, 50381, 48195, 1004, 993, 555, 457, 77, 0]

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

def printCard(n,dbfId,cardData):
    #USE FOR DEBUGGING
    if n == 1:
        mult = '1x '
    elif n == 2:
        mult = '2x '

    cardName = cardData[str(dbfId)]['name']
    print(mult + cardName)

def getName(n,dbfId,cardData):
    #TURN DBFID INTO NAME AND AMOUNT AS STRING
    if n == 1:
        mult = '1x '
    elif n == 2:
        mult = '2x '

    cardName = cardData[str(dbfId)]['name']
    return(mult + cardName)

def cardDetails(n,dbfId,cardData):
    name = cardData[str(dbfId)]['name']
    cost = cardData[str(dbfId)]['cost']

    return {
    'name':name,
    'cost':cost,
    'n':n
    }

def compare(code1,code2):

    decoded1 = decode(code1)
    decoded2 = decode(code2)

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

    #with open('cardData', 'r') as f:
    with open('/var/www/deckcompare/cardData', 'r') as f:
        #changepath
        cardData = json.load(f)

    output = [[],[],[]]

    #BUILD DECK 1
    for i in cases['2/0']:
        output[0].append(cardDetails(2, i, cardData))
    for i in cases['2/1']:
        output[0].append(cardDetails(1, i, cardData))
    for i in cases['1/0']:
        output[0].append(cardDetails(1, i, cardData))

    #BUILD CROSSOVER
    for i in cases['2/2']:
        output[1].append(cardDetails(2, i, cardData))
    for i in cases['1/1']:
        output[1].append(cardDetails(1, i, cardData))
    for i in cases['2/1']:
        output[1].append(cardDetails(1, i, cardData))
    for i in cases['1/2']:
        output[1].append(cardDetails(1, i, cardData))

    #BUILD DECK 2
    for i in cases['0/2']:
        output[2].append(cardDetails(2, i, cardData))
    for i in cases['1/2']:
        output[2].append(cardDetails(1, i, cardData))
    for i in cases['0/1']:
        output[2].append(cardDetails(1, i, cardData))


    '''print('DECK COMPARISON RESULT:')
    print('-----------------------')
    print('Cards in Deck 1:')
    for i in output[0]:
        print(i)
    print('-----------------------')
    print('Cards in both decks:')
    for i in output[1]:
        print(i)
    print('-----------------------')
    print('Cards in Deck 2:')
    for i in output[2]:
        print(i)'''

    return output
