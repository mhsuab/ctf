arg = 3350728462

# return (# of 1s in x) * 3
def func1(x):
    i = 0
    while x != 0:
        if (x & 1) != 0:
            i += 3
        x >>= 1
    return i

from collections import Counter
ans = Counter(bin(arg))['1'] * 3
print (ans, f'{ans:08x}'[-8:])
