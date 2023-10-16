from cvc5.pythonic import *

length = 8

# starting from the 98-th number in `chal.txt`
target = [
    [16774200, 1411, 16776275, 3646, 1532, 6451, 2510, 16777141],
    [16775256, 2061, 16776706, 2260, 2107, 6124, 878, 16776140],
    [16775299, 1374, 16776956, 2212, 1577, 4993, 1351, 16777040],
    [16774665, 1498, 16776379, 3062, 1593, 5966, 1924, 16776815],
    [16774318, 851, 16775763, 3663, 711, 5193, 2591, 16777069],
    [16774005, 1189, 16776283, 3892, 1372, 6362, 2910, 307],
    [16775169, 1031, 16776798, 2426, 1171, 4570, 1728, 33],
    [16775201, 819, 16776898, 2370, 1132, 4255, 1900, 347]
]

trans = [
    [-7,  -2,  -2,   9,  -2,   6,   9,   5],
    [-2,   3,  -4,   3,   2,   7,  -1,  -5],
    [3,   2,  -3,  -3,  -1,  -2,  -6,  -8],
    [-4,   5,  -3,   5,   3,  13,   1,  -6],
    [4,   6,   4,  -6,   6,   5,  -8,  -5],
    [-13, -10,  -5,  17,  -8,   1,  22,  15],
    [-2,  11,  -2,   2,   9,  20,  -6, -11],
    [-7,  -3,   6,   7,   4,   8,  13,  15]
]

# flag with maximum input of 16777216
flag = [
    [BitVec(f'flag_{i}_{j}', 24) for i in range(length)]
    for j in range(length)
]

result = [[0 for i in range(length)] for j in range(length)]
for i in range(length):
    for j in range(length):
        result[i][j] = Sum([flag[i][k] * trans[k][j] for k in range(length)])

s = Solver()
for i in range(length):
    for j in range(length):
        s.add(flag[i][j] > 32, flag[i][j] < 127, target[i][j] == result[i][j])

if s.check() == sat:
    m = s.model()
    print(''.join([chr(m[flag[i][j]].as_long() % 256)
          for i in range(length) for j in range(length)]))
else:
    print('unsat')
