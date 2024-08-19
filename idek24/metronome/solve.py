'''
./metronome < <(python3 solve.py)
'''
from struct import unpack_from

size = 0x208
with open('./metronome', 'rb') as f:
    binary = f.read()

indices = [unpack_from('<ii', binary, 0x3020 + 8 * i) for i in range(size)]
boundaries = [tuple(pow(i, 0.5) for i in unpack_from('<dd', binary, 0x4060 + 0x10 * size * i + 0x10 * i)) for i in range(size)]

'''
0 -> (0, 0)
1 -> (1, 0) or (0, 1)
2 -> (1, 1)
'''
CASE_0 = (0., 1.)
CASE_1 = (1.9, 2.1)
CASE_2 = (2.1, None)
visited = set()
initial_types = [-1 for _ in range(size)]
for idx in range(size):
    if boundaries[idx][0] >= CASE_1[1]:
        assert initial_types[idx] == -1
        initial_types[idx] = 2
        visited.add(idx)
    elif boundaries[idx][1] <= CASE_1[0]:
        assert initial_types[idx] == -1
        initial_types[idx] = 0
        visited.add(idx)
    else:
        initial_types[idx] = 1

bits = [-1 for _ in range(size)]
while not all(i != -1 for i in bits):
    for idx in range(size):
        a, b = indices[idx]
        if initial_types[idx] == 0:
            assert bits[a] == 0 or bits[a] == -1
            assert bits[b] == 0 or bits[b] == -1
            bits[a] = 0
            bits[b] = 0
        elif initial_types[idx] == 2:
            assert bits[a] == 1 or bits[a] == -1
            assert bits[b] == 1 or bits[b] == -1
            bits[a] = 1
            bits[b] = 1
        else:
            match bits[a], bits[b]:
                case (-1, -1) | (1, 0) | (0, 1):
                    pass
                case (-1, 0):
                    bits[a] = 1
                case (-1, 1):
                    bits[a] = 0
                case (0, -1):
                    bits[b] = 1
                case (1, -1):
                    bits[b] = 0
                case _:
                    assert False, f'{bits[a] = }, {bits[b] = }, {(a, b) = }'

print (int(''.join(str(i) for i in bits[::-1]), 2).to_bytes(66, byteorder='little').decode())
