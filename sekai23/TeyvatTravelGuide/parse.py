# gdb -q -x parse.py
import gdb

# run the program, genshin
gdb.execute('file genshin')

# breakpoint before pow
gdb.execute('b *0x4ABA89')
# breakpoint s.t. $rax = (value of checker)
gdb.execute('b *0x4ABBF0')

gdb.execute('r')

# set rip to after pow
gdb.execute('set $rip = $rip + 5')

gdb.execute('c')

# get inferior from gdb
inferior = gdb.inferiors()[0]

size = 48
grid_addr = gdb.parse_and_eval("$rbp - 0x488 + 0x8")
matrix = inferior.read_memory(grid_addr, size * 8 * 3)

# parse the matrix s.t. each 8 bytes is a integer
# and only keep the first integer of every 3 integers
grid_values_address = [int.from_bytes(matrix[i:i+8], byteorder='little') for i in range(0, len(matrix), 24)]

import numpy as np
import pickle

cost = np.zeros((size, size), dtype=np.int64)
for x in range(size):
    for y in range(size):
        cost[x, y] = int.from_bytes(inferior.read_memory(grid_values_address[y] + 8 * x, 8), byteorder='little', signed=True)

# save the matrix values
grids_file = 'cost.pkl'
with open(grids_file, 'wb') as f:
    pickle.dump(cost, f)

# quit gdb
gdb.execute('q')