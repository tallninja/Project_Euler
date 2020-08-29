
x = 2
y = 100

powers = []

for a in range(x, y + 1):
	for b in range(x, y + 1):
		powers.append(a ** b)

powers_set = list(set(powers))
powers_set.sort()
print(len(powers_set))

