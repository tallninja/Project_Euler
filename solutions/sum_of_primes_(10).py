lower = 1
upper = 2000000
suml = 0
for num in range(lower, upper):
    if num > 1:
        for n in range(2, num):
            if num % n == 0:
                break

        else:
            suml += num

print(suml)
