from enum import Enum
from dataclasses import dataclass

with open('chal.bin', 'rb') as f:
    f.seek(0x40)
    raw = f.read()
prog = [raw[i:i+5] for i in range(0, len(raw), 5)][:-1]

class MODE(Enum):
    NEXT = 0
    COND = 1
    FLAG = 2
    END = 3

    def __repr__(self) -> str:
        return self.name

@dataclass
class struct:
    index: int
    mode: MODE
    check_idx: int
    flag_idx: int
    jump: int
    next: int
    term: int

def trans(i):
    x = prog[i]
    mode = x[0] >> 2
    return struct(
        index = i,
        mode = MODE.END if mode >= 3 else MODE(mode),
        check_idx = int((x[0] & 2) != 0),
        flag_idx = int(x[0] & 1),
        jump = int.from_bytes(x[1:3], byteorder='little'),
        next = x[3],
        term = x[4],
    )
prog = list(map(trans, range(len(prog))))

start = False
counter = 0
jump_target = None
flag = ''
for (i, p) in enumerate(prog):
    if not start:
        if p.mode == 'FLAG':
            start = True
            counter = 0
            jump_target = None
    else:
        if jump_target is None:
            if p.mode == 'COND':
                jump_target = p.jump
                counter += 1
        elif jump_target == p.jump:
            counter += 1
        else:
            flag += chr(counter)
            start = False

print (flag)
