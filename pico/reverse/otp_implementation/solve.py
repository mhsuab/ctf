from Crypto.Util.number import long_to_bytes

expected = b'lfmhjmnahapkechbanheabbfjladhbplbnfaijdajpnljecghmoafbljlaamhpaheonlmnpmaddhngbgbhobgnofjgeaomadbidl'

with open('flag.txt', 'r') as f:
    raw = f.read()

key = 'd5bd1989bcfd57a5fe5e680221a92576364d485ec3777d728a11a6571a06d48be5f7881e29023cdad3b9ab8b2e7677297bd4'

print (long_to_bytes(int(raw, 16) ^ int(key, 16)).decode())
