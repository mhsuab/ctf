'''
'''
import gmpy2
from Crypto.Util.number import long_to_bytes

with open('public-key.txt', 'r') as f:
    raw = f.readlines()

n1 = gmpy2.mpz(raw[0].split()[-1])
n2 = gmpy2.mpz(raw[1].split()[-1])
n3 = gmpy2.mpz(raw[2].split()[-1])
e = gmpy2.mpz(raw[3].split()[-1])
c = gmpy2.mpz(raw[4].split()[-1])

p = gmpy2.gcd(n1, n2)
q = gmpy2.divexact(n1, p)
r = gmpy2.divexact(n2, p)
assert(n3 == q * r)

flag = c

for _pair in [(q, r), (p, r), (p, q)]:
    phi = (_pair[0] - 1) * (_pair[1] - 1)
    d = pow(e, -1, phi)
    flag = pow(flag, d, _pair[0] * _pair[1])

print (long_to_bytes(flag))