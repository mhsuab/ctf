# python3 solve.py | nc ctf.b01lers.com 5210

def keygen(s):
    if len(s) < 10:
        raise ValueError("Input should have length at least 9")
    ss = [int(i) for i in s]
    result = 0
    for (i, v) in enumerate(ss):
        if (i & 1) == 0:
            v = v * 2
            v = [int(j) for j in str(v)]
            v = sum(v)
        result += v
    return s + str((10 * (result // 10) - result + 10) % 10)

from random import randint
print (keygen(str(randint(10000000000, 99999999999))))
