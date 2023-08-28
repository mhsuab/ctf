#!python3 solve.py
from pwn import *
import subprocess
import numpy as np
import pickle
from tqdm import tqdm
from const import *

elf = ELF(binary_path)

if not os.path.exists(filename):
    # run `gdb -q -x parse.py`
    subprocess.run(['gdb', '--batch-silent', '-x', 'parse.py'])
with open(filename, 'rb') as f:
    cost = pickle.load(f)

size = 48
checker = 333
checker_target = 1
checkers = np.zeros((size, size), dtype=np.int64)
checkers[0, 0] = checker
paths = {(0, 0): ''}

for idx in range(1, size):
    checkers[idx, 0] = cost[idx, 0] + checkers[idx - 1, 0]
    paths[(idx, 0)] = paths[(idx - 1, 0)] + R
    checkers[0, idx] = cost[0, idx] + checkers[0, idx - 1]
    paths[(0, idx)] = paths[(0, idx - 1)] + D

for x in range(1, size):
    for y in range(1, size):
        checkers[x, y] = cost[x, y] + max(checkers[x - 1, y], checkers[x, y - 1])
        if checkers[x - 1, y] > checkers[x, y - 1]:
            paths[(x, y)] = paths[(x - 1, y)] + R
        else:
            paths[(x, y)] = paths[(x, y - 1)] + D

if checkers[size - 1, size - 1] != checker_target:
    print(f'Solution not found (maximum value of the bottom right cell is not {checker_target})')
    exit()

path = paths[(size - 1, size - 1)]

# nc chals.sekai.team 7000
r = remote('chals.sekai.team', 7000)

r.recvuntil(b'work: ')
pow = r.recvline().strip()
sol = subprocess.check_output(pow, shell=True).strip()
r.sendline(sol)
r.recvuntil(b'...\n')

for c in tqdm(path):
    r.recvlines(2 * size + 1)
    r.sendline(c.encode())

r.recvuntil(b'...\n')
flag = r.recvline().strip().decode()
print(flag)
# SEKAI{Klee_was_a_brave_girl_today!_I_found_a_really_weird-looking_lizard!_Want_me_to_show_it_to_you?}
