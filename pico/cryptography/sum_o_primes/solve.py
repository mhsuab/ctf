'''
quadratic formula

x = p + q
n = pq
-> p^2 - xp + n = 0
'''
import gmpy2
from Crypto.Util.number import long_to_bytes

with open('output.txt', 'r') as f:
    raw = f.readlines()

x = gmpy2.mpz(raw[0].split()[-1], base = 16)
n = gmpy2.mpz(raw[1].split()[-1], base = 16)
c = gmpy2.mpz(raw[2].split()[-1], base = 16)

x_square = gmpy2.square(x)
four_n = gmpy2.mul(4, n)
discriminant = gmpy2.sub(x_square, four_n)
discriminant_sqrt = gmpy2.isqrt(discriminant)

p = gmpy2.divexact(gmpy2.add(x, discriminant_sqrt), 2)
q = gmpy2.divexact(gmpy2.sub(x, discriminant_sqrt), 2)

assert(n == gmpy2.mul(p, q))
assert(x == gmpy2.add(p, q))

e = 65537
m = gmpy2.lcm(p - 1, q - 1)
d = pow(e, -1, m)
flag = pow(c, d, n)

print (long_to_bytes(flag).decode())
