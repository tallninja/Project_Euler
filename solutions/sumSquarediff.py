# The sum of the squares of the first ten natural numbers is,

# 12+22+...+102=385
# The square of the sum of the first ten natural numbers is,

# (1+2+...+10)2=552=3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sumSqr = 0
suml = 0

for i in range(1, 101):
    sqr = i**2
    sumSqr += sqr

for j in range(1, 101):
    suml += j

sqrSum = suml**2

print(sqrSum - sumSqr)
