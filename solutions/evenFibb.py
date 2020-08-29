# calculates the sum of all even numbers in the fibonacci sequence <= 4000000

a = 1
b = 1
c = 0
sum = 0

while c <= 4000000:
    print(a)
    c = a + b
    a = b
    b = c

    if a % 2 == 0:
        sum += a

print(f"\n {sum}")
