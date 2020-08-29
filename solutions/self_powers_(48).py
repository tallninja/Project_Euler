
suml = 0
for i in range(1, 1001):
    powr = i ** i
    suml += powr

strSuml = str(suml)
ans = strSuml[-10:]

print(ans)
