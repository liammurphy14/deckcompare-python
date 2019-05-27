import base64
#test1
#example deck code to work with
#deckcode = "AAECAZ8FBJ74AoPUAqcFrwQNteYC1uUC0eEC+9MClc4C48sCuMcCg8cC68IC m8IC+Qr1BUYA"
deckcode = "AAEBAZICCMQGi68Cya8CorYCoM4Cws4Cy+wCzfQCC0DkCMuvAs+vAtCvAuKvAs6xAqDNAofOAp7SAurmAgA="
#deckcode = input("Please enter a deck code:  ")

def decode(deckcode):
    #decode base64 encoded string
    code = base64.b64decode(deckcode)

    #result:
    # b'\x00\x01\x02\x01\xfd\x04\x08\xa3\xeb\x02\xf2\xd3\x02\x9b\xd3\x02\xc2\xce\x02\xa0\xce\x02\xd3\xc5\x02\xd0\x02\x9c\x02\x0b\xb7\xf1\x02\xbe\xec\x02\x96\xe4\x02\xd7\xe1\x02\xd5\xe1\x02\x96\xc7\x02\x9b\xc2\x02\xec\x07\xc9\x03\x8a\x01M\x00'

    #convert hex to binary
    binCode = []
    for i in range(len(code)):
        binCode.append(format(code[i], "08b"))

    #decode dem varints
    final = []

    i = 0
    while i < len(binCode):
        group = []

        x = 1
        while x:
            group.append(binCode[i])
            if binCode[i][0] == "1":
                i += 1
            else:
                x = 0
        i += 1

        combined = ""
        for j in range(len(group)):
            combined += group[-j-1][1:]
        final.append(combined)

    for i in range(len(final)):
        final[i] = int(final[i], 2)

    return final



#Result example: [0, 1, 2, 1, 671, 4, 48158, 43523, 679, 559, 13, 45877, 45782, 45265, 43515, 42773, 42467, 41912, 41859, 41323, 41243, 1401, 757, 70, 0]
