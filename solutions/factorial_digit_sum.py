def factorial(num):
    fact = 1
    suml = 0
    for i in range(1, num + 1):
        fact *= i
    strFact = str(fact)
    for dig in strFact:
        num = int(dig)
        suml += num

    return suml


print(factorial(100))
