from vennComp import compare
import json

deckA = "AAECAaoICP4Figfv9wKZ+wLLhQPFmQPjtAPTwAMLnAKBBP8Fsgaw8ALPpQO3rQO5rQP+rgOqrwPQrwMA"
deckB = "AAECAaoICpQD/gWKB+/3Apn7AsuFA8WZA9aZA+O0A9PAAwr/BbIGsPACjIUDtJcDt60Dua0D/q4Dqq8D0K8DAA=="
venn = compare(deckA, deckB)

with open('cardData', 'r') as f:
    cardList = json.load(f)

def printNames(list):
    for i in range(2):
        for j in range(len(list[i])):
            cardName = cardList[str(list[i][j])]['name']
            print(str(i+1) + "x " + cardName)

print("---------------------")
print("Cards only in Deck 1:")
print("---------------------")
printNames(venn[0])
print("---------------------")
print("Cards in both decks:")
print("---------------------")
printNames(venn[1])
print("---------------------")
print("Cards only in Deck 2:")
print("---------------------")
printNames(venn[2])
print("---------------------")
