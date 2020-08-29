import string

with open('p022_names.txt', 'r') as namesList:
    names = namesList.read()
    nmArr = names.split(",")
    nmArr.sort()  # sorts the names alphabetically
    alphabet = string.ascii_uppercase
    sumArr = []
    marks = []
    total = 0

    for name in nmArr:
        suml = 0
        for letter in name:
            if letter in alphabet:
                pos = alphabet.find(letter)
                suml += (pos + 1)
        sumArr.append(suml)

    for i in range(len(nmArr)):
        mark = (i + 1) * sumArr[i]
        marks.append(mark)

    for mark in marks:
        total += mark

    print(total)
