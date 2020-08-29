

def collatz(n):
	collatz_sequence = [n]

	while True:
		if  n > 1:
			if n % 2 == 0:
				n /= 2
				collatz_sequence.append(int(n))
			else:
				n = (n * 3) + 1
				collatz_sequence.append(int(n))
		else:
			break

	return collatz_sequence

i = 1
limit = 1000000
largest = [0, 0]

while i < limit:
	if len(collatz(i)) > largest[1]:
		largest[0] = i
		largest[1] = len(collatz(i))

	i += 1

print(largest)
