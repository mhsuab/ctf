import numpy as np

with open('message.txt', 'r') as f:
    pt = f.read()

N = 4
L = len(pt)

rail_fence = np.array([['' for _ in range(L)] for _ in range(N)])

i = 0
j = 0

def next_dist(distance):
    if distance == 2:
        return 4
    elif distance == 4:
        return 2
    else:
        return 6

for c in pt:
    if i < N:
        distance = 6
        if j == 1:
            distance = 4
        elif j == 2:
            distance = 2
    else:
        distance = next_dist(distance)
    rail_fence[j][i] = c
    i += distance
    if i >= L:
        j += 1
        i = j

print (''.join(rail_fence.flatten(order = 'F')))