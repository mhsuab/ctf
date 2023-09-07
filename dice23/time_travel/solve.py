from pwn import *
import numpy as np

iter = 64

def parse(filename):
    with open(filename, 'rb') as f:
        raw = f.read()

    size = u32(raw[:4])
    raw = [u64(raw[i: i + 8], sign='signed') for i in range(4, len(raw), 8)]
    raw = np.array(raw, dtype=np.int64).reshape((iter, -1))

    return size, raw[:, -1], raw[:, -1].reshape((-1, size, size))

size, ct, matrices = parse('input.bin')

flag = ''
ret = []
for i in range(64):
    det = np.rint(np.linalg.det(matrices[i]))
    _ret = chr(ct[i] - int(det) + i)
    flag += _ret
print (flag)
