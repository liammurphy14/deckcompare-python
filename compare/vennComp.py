import decoder

def organise(deck): #function to extract card dbfIDs from decoded decklist

    list1 = []
    list1.append(deck[6:6+deck[5]])
    list1.append(deck[7+deck[5]:7+deck[5]+deck[6+deck[5]]])

    list2 = []
    for i in range(len(list1[0])):
        list2.append(list1[0][i])

    for i in range(len(list1[1])):
        list2.append(list1[1][i])

    both = [list1, list2]
    return both

def checkDoubles(inDeck, list1):
    for i in range(len(inDeck)):
        if inDeck[i] in list1[1]:
            inDeck.append(inDeck[i])

def compare(deckOne, deckTwo):

    #runs decoder function to end up with list of IDs
    deckOne = decoder.decode(deckOne)
    deckTwo = decoder.decode(deckTwo)

    #organise(deckOne)
    #organise(deckTwo)

    deckOneBoth = organise(deckOne)
    deckTwoBoth = organise(deckTwo)

    # deckXA two lists of single and double cards deckXB list of all cards
    deckOneA = deckOneBoth[0]
    deckOneB = deckOneBoth[1]

    deckTwoA = deckTwoBoth[0]
    deckTwoB = deckTwoBoth[1]

    # Turn list2 into sets and compare and then turn the output back into a list
    inOne = list(set(deckOneB) - set(deckTwoB))
    inTwo = list(set(deckTwoB) - set(deckOneB))




    checkDoubles(inOne, deckOneA)
    checkDoubles(inTwo, deckTwoA)

    inBoth = []


    inCommon = list(set(deckOneB) & set(deckTwoB))
    #print(inCommon)

    for i in range(len(inCommon)):
        # if both cards are singles
        if inCommon[i] in deckOneA[0] and inCommon[i] in deckTwoA[0]:
            inBoth.append(inCommon[i])
        # if single in deck1 but double in deck2
        elif inCommon[i] in deckOneA[0] and inCommon[i] not in deckTwoA[0]:
            inBoth.append(inCommon[i])
            inTwo.append(inCommon[i])
        # if double in deck1 but single in deck2
        elif inCommon[i] not in deckOneA[0] and inCommon[i] in deckTwoA[0]:
            inBoth.append(inCommon[i])
            inOne.append(inCommon[i])
        # if double in both
        elif inCommon[i] in deckOneA[1] and inCommon[i] in deckTwoA[1]:
            inBoth.append(inCommon[i])
            inBoth.append(inCommon[i])
        else:
            print("Check for card in set went wrong")


    return[inOne, inBoth, inTwo]

#Example Usage:

#deckOne = "AAECAZ8FBJ74ApXOAqcFrwQN/eoCteYC1uUC0eEC+9MC48sCuMcCg8cC68IC m8IC+Qr1BUYA"
#deckTwo = "AAECAZ8FBp74Av3qApvCApcGpwWvBAy15gLW5QLR4QL70wKVzgLjywK4xwKD xwLrwgL5CvUFRgA="
#print(compare(deckOne, deckTwo))
