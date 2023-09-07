'''
Pohlig–Hellman algorithm
(works when p-1 has small factors)

-> pollard (solve p, q) + discrete_log + crt
'''
import gmpy2
from Crypto.Util.number import long_to_bytes
from sympy.ntheory import discrete_log
from sympy.ntheory.modular import crt

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

cp = c % p
cq = c % q

xp = discrete_log(p, cp, 3)
xq = discrete_log(q, cq, 3)

flag, pq = crt([p, q], [xp, xq])
assert(pq == n)
print (long_to_bytes(flag).decode())