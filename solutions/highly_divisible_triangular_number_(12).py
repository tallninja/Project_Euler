
not_reached_500 = True
limit = 1

def factor_generator(number):
	factors = []

	for i in range(1, number + 1):
		if number % i == 0:
			factors.append(i)
	return factors


while not_reached_500:
	for i in range(0, limit):
		x = [j for j in range(0, i + 1)]
		number = sum(x)

		factors = factor_generator(number)

	if len(factors) > 500:
		print(f"{number}:{factors}:{len(factors)}")
		break
	else:
		limit += 1
