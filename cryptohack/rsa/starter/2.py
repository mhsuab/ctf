m = 12
e = 65537
p = 17
q = 23

phi = (p - 1) * (q - 1)
n = p * q
d = pow(e, -1, phi)

c = pow(m, e, n)
print (f'{c = }')

