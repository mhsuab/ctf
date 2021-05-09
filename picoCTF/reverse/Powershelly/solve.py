from rev import rev
from string import printable

_input = [i.split(' ') for i in rev().split('\r\n')]

for i in _input:
    f = lambda s: '0' if s == i[0] else '1'
    count = 0
    flag_binary = []
    for j in i:
        if count % 8:
            flag_binary[-1] += f(j)
        else:
            flag_binary.append(f(j))
        count += 1
    print (''.join(chr(int(i, 2)) for i in flag_binary))