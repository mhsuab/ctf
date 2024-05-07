import numpy as np

lut = { (0, 0): 0, (0, 1): 0, (0, 2): 0, (0, 3): 0, (0, 4): 1, (0, 5): 1, (0, 6): 2, (0, 7): 2,
       (1, 0): -1, (1, 1): 3, (1, 2): 4, (1, 3): 4, (1, 4): 1, (1, 5): 2, (1, 6): 2, (1, 7): 2,
       (2, 0): -1, (2, 1): 3, (2, 2): 3, (2, 3): 4, (2, 4): 1, (2, 5): 5, (2, 6): 5, (2, 7): 5,
       (3, 0): -1, (3, 1): 3, (3, 2): 4, (3, 3): 4, (3, 4): 4, (3, 5): 5, (3, 6): 5, (3, 7): 5,
       (4, 0): 6, (4, 1): 6, (4, 2): 6, (4, 3): 7, (4, 4): 7, (4, 5): 7, (4, 6): 7, (4, 7): -1,
       (5, 0): 8, (5, 1): 6, (5, 2): 9, (5, 3): 9, (5, 4): 10, (5, 5): 10, (5, 6): 10, (5, 7): 10,
       (6, 0): 8, (6, 1): 6, (6, 2): 9, (6, 3): 11, (6, 4): 11, (6, 5): 11, (6, 6): -1, (6, 7): 12,
       (7, 0): 8, (7, 1): 8, (7, 2): 9, (7, 3): 9, (7, 4): 11, (7, 5): 12, (7, 6): 12, (7, 7): 12 }

# hand solved...
path = [(0, 0), (0, 1), (0, 2), (1, 2), (1, 1), (2, 1), (2, 2), (2, 3),
        (1, 3), (0 ,3), (0, 4), (1, 4), (2, 4), (2, 5), (2, 6), (1, 6),
        (1, 5), (0, 5), (0, 6), (0, 7), (1, 7), (2, 7), (3, 7), (3, 6),
        (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (6, 6), (5, 6),
        (5, 5), (5, 4), (5, 3), (5, 2), (6, 2), (6, 3), (6, 4), (6, 5),
        (7, 5), (7, 4), (7, 3), (7, 2), (7, 1), (7, 0), (6, 0), (6, 1),
        (5, 1), (5, 0), (4, 0), (4, 1) ,(4, 2), (4, 3), (4, 4), (4, 5),
        (3, 5), (3, 4), (3, 3), (3, 2), (3, 1), (3, 0), (2, 0), (1, 0)]
path.append((0, 0))

# m = np.zeros((8, 8))
m = np.full((8, 8), -2)
for ((x, y), v) in lut.items():
    m[y, x] = v
print (m)

data = [-1] * 64

indices_A = [0, 0, 0, 1, 1, 2]
indices_B = [1, 2, 3, 2, 3, 3]

delta_X_list = [-1, 0, 1, 0]
delta_Y_list = [0, 1, 0, -1]

X, Y = 0, 0
checkers = [0] * 13
counter = 0
delta_X, delta_Y = -1, 0
prev = 0

def find_value(x, y, dx, dy, nx, ny):
    valid = {}
    peek = -1

    for i in range(6):
        a = indices_A[i]
        b = indices_B[i]

        dx_a, dy_a = delta_X_list[a], delta_Y_list[a]
        dx_b, dy_b = delta_X_list[b], delta_Y_list[b]

        A = bool((dx_a + dx) or (dy_a + dy))
        B = bool((dx_b + dx) or (dy_b + dy))

        if A and B:
            continue
        elif A:
            if 0 <= (x + dx_a) < 8 and 0 <= (y + dy_a) < 8:
                if x + dx_a == nx and y + dy_a == ny:
                    return i, dx_a, dy_a
                peek = lut[(x + dx_a, y + dy_a)]
                valid[peek] = (i, dx_a, dy_a)
        else:
            if 0 <= (x + dx_b) < 8 and 0 <= (y + dy_b) < 8:
                if x + dx_b == nx and y + dy_b == ny:
                    return i, dx_b, dy_b
                peek = lut[(x + dx_b, y + dy_b)]
                valid[peek] = (i, dx_b, dy_b)

    assert False, f'{x = }, {y = }, {nx = }, {ny = }, {valid = }'

for (nx, ny) in path[1:]:
    data[8 * X + Y], delta_X, delta_Y = find_value(X, Y, delta_X, delta_Y, nx, ny)
    cur = lut[(X, Y)]

    if ((prev & cur) != -1):
        if (cur == prev):
            counter += 1
            if counter > 3:
                1/0
        else:
            if checkers[prev] < counter:
                checkers[prev] = counter
            counter = 1

    X += delta_X
    Y += delta_Y
    prev = cur

if not all([c == 3 for c in checkers]) or not all([d != -1 for d in data]):
    2/0

chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
data_offsets = [4, 7, 11, 0, 32, 9, 13, 28, 6, 21, 13, 13, 5, 31, 22, 20, 3, 33, 7, 34, 14, 5, 31, 7, 23, 18, 15, 11, 16, 9, 22, 7]
assert len(data_offsets) == 32 and len(chars) == 36

f = lambda i: chars[(data[2 * i] * 6 + data[2 * i + 1] - data_offsets[i]) % 36]
flag = f'dice{{{"".join(f(i) for i in range(32))}}}'
print (f'{flag = }')
