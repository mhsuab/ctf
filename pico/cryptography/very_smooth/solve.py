'''
(p - 1), (q - 1) -> smooth number

[Pollard's p − 1 algorithm](https://en.wikipedia.org/wiki/Pollard%27s_p_%E2%88%92_1_algorithm)
'''
import gmpy2
from Crypto.Util.number import long_to_bytes

import sys
sys.path.append('../../../utils/cryptography')
from pollard_factorization import pollard_factorization

with open('output.txt', 'r') as f:
    raw = f.readlines()

n = gmpy2.mpz(raw[0].split()[-1], base = 16)
c = gmpy2.mpz(raw[1].split()[-1], base = 16)

p = pollard_factorization(n, gmpy2.mpz(2) ** 16)
assert(n.is_divisible(p))
q = gmpy2.divexact(n, p)

e = 0x10001
m = gmpy2.lcm(p - 1, q - 1)
d = pow(e, -1, m)
flag = pow(c, d, n)

print (long_to_bytes(flag).decode())
