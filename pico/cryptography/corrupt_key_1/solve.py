import gmpy2
from Crypto.Util.number import long_to_bytes
from Crypto.PublicKey import RSA

key = RSA.importKey(open('private.key').read())
print (hex(key.n))
print (hex(key.p))
assert(key.n % key.p == 0)