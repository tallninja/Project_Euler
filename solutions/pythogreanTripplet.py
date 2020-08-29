# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

lim = 100
for i in range(1, lim):
    for j in range(1, lim):
        for k in range(1, lim):
            suml = i + j + k
            if suml != 1000:
                lim += 100
            else:
                print(f"{i} + {j} + {k} = {suml}")
