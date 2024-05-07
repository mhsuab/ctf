from struct import unpack
from collections import defaultdict

def get_visited_index(s: str):
    idx = s[s.find('<visited') + 8:s.find('>')]
    if idx == '':
        return 0
    return int(idx, 16) // 4

with open('./koenigsberg', 'rb') as f:
    raw = f.read()

func = raw[0x94020:0xb3420]
func = [unpack('<Q', func[i: i + 8])[0] for i in range(0, len(func), 8)]
func_size = 0x3e80

with open('./koenigsberg_check_path.asm', 'r') as f:
    asm = f.readlines()

asm = [s.strip().split(':') for s in asm]
asm = { int(s[0], 16): s[1].strip() for s in asm }

path = {}
targets = defaultdict(lambda: set())
params = {}
params[0] = (0x35, 0)

for (idx, i) in enumerate(func):
    key = get_visited_index(asm[i + 21])
    value = get_visited_index(asm[i + 27])
    xor = int(asm[i + 95].split(',')[-1], 16)
    add = int(asm[i + 111].split('+')[-1][:-1], 16)

    if key in path and path[key] != value:
        assert False, "lead to different value"
    else:
        path[key] = value
        targets[value].add(idx)
        params[value] = (xor, add)

from string import printable

cur = 0
visited = []
count = 0
flag = ''
while cur not in visited:
    visited.append(cur)

    xor, add = params[cur]

    cur = path[cur]
    for c in printable:
        if (((ord(c) ^ xor) + add) % func_size) in targets[cur]:
            flag += c
            break

    count += 1
    if count >= 68:
        break

print(flag)
# srdnlen{uhm_technically_this_is_a_hamiltonian_cycle_:nerd:_0ff829a6}
