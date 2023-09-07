with open('output.txt', 'r') as f:
    raw = f.read()
ct = bytes.fromhex(raw)

def decrypt(ptxt, key):
    ctxt = b''
    for i in range(len(ptxt)):
        a = ptxt[i]
        b = key[i % len(key)]
        ctxt += bytes([a ^ b])
    return ctxt

random_strs = [
    b'my encryption method',
    b'is absolutely impenetrable',
    b'and you will never',
    b'ever',
    b'ever',
    b'ever',
    b'ever',
    b'ever',
    b'ever',
    b'break it'
]

possibilities = [ct]

for r in random_strs:
    possibilities += [decrypt(p, r) for p in possibilities]

# find possiblt key
for p in possibilities:
    # print (decrypt(b'picoCTF{', p))
    pt = decrypt(b'picoCTF{', p)
    if pt[1:].find(pt[0]) != -1:
        print (pt[1:].find(pt[0]), pt)

# actually decrypt
possible_key = b'Africa!'
for p in possibilities:
    pt = decrypt(p, possible_key)
    if b'picoCTF{' in pt:
        print (pt)