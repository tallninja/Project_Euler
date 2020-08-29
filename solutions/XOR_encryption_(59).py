import string
from itertools import combinations_with_replacement

alphabet = string.ascii_lowercase


with open('p059_cipher.txt', 'r') as text:
    cipher = text.read()
    cipherArr = cipher.split(",")
    letterArr = []
    asciiAlphabet = []
    key = "cat"
    keyArr = ""

    for i in alphabet:
        letter = ord(i)
        asciiAlphabet.append(letter)

    cipherLen = len(cipherArr)
    for i in range(cipherLen):
        for letter in key:
            keyArr += letter
        cipherLen /= len(key)

    print(len(keyArr))
    print(len(cipherArr))
