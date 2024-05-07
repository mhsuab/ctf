from math import gcd

def prim_roots(modulo):
    coprime_set = {x for x in range(1, modulo) if gcd(x, modulo) == 1}
    # return [g for g in range(1, modulo) if coprime_set == {pow(g, powers, modulo) for powers in range(1, modulo)}]
    for g in range(1, modulo):
        if coprime_set == { pow(g, powers, modulo) for powers in range(1, modulo) }:
            return g
    return None

p = 28151
print (prim_roots(p))

# fp = GF(p, modulus="primitive")
# smallest_prim_element = fp.gen()

