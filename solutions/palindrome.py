
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

a = 100
b = 999
palindromes = []
palindromesInt = []

# bruteforcing the problem and appending the palindromes to a list
for i in range(a, b):
    for j in range(a, b):

        pal = i * j
        strPal = str(pal)

        if strPal == strPal[::-1]:
            palindromes.append(strPal)

        else:
            pass

# converts the srings in the list to integers
for string in palindromes:
    num = int(string)
    palindromesInt.append(num)

# sorts the list and reverses the order
palindromesInt.sort(reverse=True)
strPalLargest = palindromesInt[0]

print(
    f"The largest palindrome made from the product of two 3-digit numbers is: {strPalLargest}")
