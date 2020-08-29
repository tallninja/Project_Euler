import string

with open('p042_words.txt', 'r') as nameFile:
    names = nameFile.read()
    alphabet = string.ascii_uppercase
    smAlpahabet = 0
    nmArr = names.split(",")
    totals = []
    triangles = []
    answer = []
    for name in nmArr:
        total = 0
        for letter in name:
            if letter in alphabet:
                pos = alphabet.find(letter) + 1
                total += pos

        totals.append(total)

    for n in range(len(alphabet) + 1):
        triangle = int((1 / 2) * n * (n + 1))
        triangles.append(triangle)

    for t in totals:
        if t in triangles:
            answer.append(t)

    print(f"There are {len(answer)} triangle names")
