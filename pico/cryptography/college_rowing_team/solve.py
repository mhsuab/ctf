'''
c1 = pow(m, e, n1)
c2 = pow(m, e, n2)
c3 = pow(m, e, n3)

m3 = crt([n], [c])
m3 < n1 * n2 * n3
'''
import gmpy2
from itertools import combinations
from Crypto.Util.number import long_to_bytes, bytes_to_long
from sympy.ntheory.modular import crt

with open('encrypted-messages.txt', 'r') as f:
    raw = f.readlines()

e = 3
n = []
c = []

for i in range(0, len(raw), 4):
    n.append(gmpy2.mpz(raw[i + 0].split()[-1]))
    c.append(gmpy2.mpz(raw[i + 2].split()[-1]))

msgs = [
    b'I just cannot wait for rowing practice today!',
    b'I hope we win that big rowing match next week!',
    b'Rowing is such a fun sport!'
        ]

for i, j, k in combinations(range(len(n)), 3):
    m3, _ = crt([n[i], n[j], n[k]], [c[i], c[j], c[k]])
    m, exact = gmpy2.iroot(m3, e)
    flag = long_to_bytes(m)
    if exact and (flag not in msgs):
        print (flag.decode())
