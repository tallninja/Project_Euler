lower = 1
upper = 1000
primes = []

while len(primes) <= 10000:
    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break

            else:
                primes.append(num)

    lower = upper + 1
    upper += 1000

print(primes)
