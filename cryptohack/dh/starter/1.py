p = 991
g = 209

# g * d mod 991 = 1
d = pow(g, -1, p)
print (f'{d = }')
assert (g * d) % p == 1

