import decoder

def deckListBuilder(deckcode):
    #turns deckcode into list of singles and doubles
    deck = decoder.decode(deckcode)

    singles = deck[6:6+deck[5]]
    doubles = deck[7+deck[5]:7+deck[5]+deck[6+deck[5]]]
    cardList = [singles,doubles]

    return cardList

def getAllCards(cardLists):
    #returns list of all unique cards across both decks for iteration
    decks = []
    for card in cardLists:
        if card not in decks:
            decks.append(card)
    return decks


def compare(deckcodeA, deckcodeB):

    #runs decoder function to end up with list of IDs
    deckA = deckListBuilder(deckcodeA)
    deckB = deckListBuilder(deckcodeB)

    decks = getAllCards(deckA[0] + deckA[1] + deckB[0] + deckB[1])
    inA = [[],[]]
    inB = [[],[]]
    inBoth = [[],[]]
    #print(decks)
    for card in decks:
        if card in deckA[0]:
            if card in deckB[0]:
                #1 in each deck
                inBoth[0].append(card)

            elif card in deckB[1]:
                #1 in A, 2 in B
                inBoth[0].append(card)
                inB[0].append(card)

            else:
                #1 in A
                inA[0].append(card)

        elif card in deckA[1]:
            if card in deckB[0]:
                #2 in A, 1 in B
                inA[0].append(card)
                inBoth[0].append(card)

            elif card in deckB[1]:
                #2 in each deck
                inBoth[1].append(card)

            else:
                #2 in A
                inA[1].append(card)

        else:
            if card in deckB[0]:
                #1 in B
                inB[0].append(card)

            elif card in deckB[1]:
                #2 in B
                inB[1].append(card)

            else:
                raise Exception("You shouldn't be here. Card: " + str(card))





    return [inA, inBoth, inB]

#Example Usage:

#deckOne = "AAECAZ8FBJ74ApXOAqcFrwQN/eoCteYC1uUC0eEC+9MC48sCuMcCg8cC68IC m8IC+Qr1BUYA"
#deckTwo = "AAECAZ8FBp74Av3qApvCApcGpwWvBAy15gLW5QLR4QL70wKVzgLjywK4xwKD xwLrwgL5CvUFRgA="
#print(compare(deckOne, deckTwo))
