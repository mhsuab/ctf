'''
https://en.wikipedia.org/wiki/Pollard%27s_p_%E2%88%92_1_algorithm
https://www.untruth.org/~josh/math/pollard-p-1.pdf
'''
import gmpy2

def pollard_factorization(n: gmpy2.mpz, smoothness: gmpy2.mpz):
    a = 2
    i = 2

    while i <= smoothness:
        print (i, end='\r')
        a = gmpy2.powmod(a, i, n)
        d = gmpy2.gcd(a - 1, n)
        if (d > 1) and (d < n):
            return d
        i += 1

    return 0