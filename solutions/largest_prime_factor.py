import math


def primeFactors(num):
    primes = []
    while num % 2 == 0:
        num /= 2

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            primes.append(i)
            num /= i
    print(f"The largets prime factor of {num} is :>>>:\t {primes[-1]}")


primeFactors(600851475143)
