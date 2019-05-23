from vennComp import compare
import json

deckOne = "AAECAf0ECIqeA6CbA5aaA62HA6iHA6CAA77sAqsEC9OYA4OWA82JA5n/AsP4 AsXzAuwHywTJA4oBTQA="
deckTwo = "AAECAf0ECoqeA5aaA4OWA6+HA6iHA6aHA6CAA8XzAooHigEKwpkD05gD55UD zYkDw/gC7AfhB6sEyQNNAA=="
venn = compare(deckOne, deckTwo)

#print(venn)

with open('cardlist', 'r') as f:
    cardList = json.load(f)

#[[493, 51781, 493, 51781, 381], [64, 64, 51779, 51779, 836, 836, 742, 742, 52809, 52810, 52810, 51790, 51790, 47063, 47063, 52819, 52819, 52438, 503, 503, 50042, 50042, 381, 48607, 48607], [49164, 43310, 52935, 49164, 52935]]

print(venn)

def printNames(n):
    for i in range(len(venn[n])):
        cardName = cardList[str(venn[n][i])]['name']
        if i != len(venn[n])-1:
            if venn[n][i] == venn[n][i+1]:
                print("2x " + cardName)
            elif venn[n][i] != venn[n][i-1]:
                print("1x " + cardName)
        elif venn[n][i] != venn[n][i-1]:
            print("1x " + cardName)

print("---------------------")
print("Cards only in Deck 1:")
print("---------------------")
printNames(0)
print("---------------------")
print("Cards in both decks:")
print("---------------------")
printNames(1)
print("---------------------")
print("Cards only in Deck 2:")
print("---------------------")
printNames(2)
print("---------------------")
