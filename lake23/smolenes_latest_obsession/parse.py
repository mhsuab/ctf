from dataclasses import dataclass, field
from typing import Dict, List, Tuple

challenge_path = './challenge/chal'
prompt_mem_dump = './chal.bss'
output_prog = 'chal.forth'

@dataclass
class FuncDefn:
    prev: Tuple[int, str]
    symbol_addr: int = 0
    name: str = ''
    funcs: List[Tuple[str, str | int]] = field(default_factory = lambda: [])

    def __str__(self) -> str:
        _f = "\n".join(f'{f[0]}\t\t\t\t{f[1]}' for f in self.funcs)
        return f'{hex(self.prev[0])}\t\t{self.prev[1]} [&prev]\n{hex(self.symbol_addr)}\t\t{self.name}\n{_f}\n'

def parse(raw: bytes, start_addr: int, to_match: int, funcs: List[FuncDefn], lut: Dict[int, str]):
    mode_name = False
    name = b''
    current = FuncDefn(prev=(0, ''))
    
    i = 0
    while i < len(raw):
        if mode_name:
            _name = raw[i: i + 16].strip(b'\x00').decode()
            name = f'fn_{{{_name}}}'
            current.name = name
            current.symbol_addr = start_addr + i
            mode_name = False
            i += 16
            lut[start_addr + i] = name
            continue
        addr = int.from_bytes(raw[i: i + 4], 'little')
        if raw[i: i + 32] == b'\x00' * 32 and len(funcs) != 0:
            if current.prev[1] != '':
                funcs.append(current)
            break
        if addr == to_match:
            if current.prev[1] != '':
                funcs.append(current)
            current = FuncDefn(prev=(start_addr + i, hex(addr)))
            to_match = start_addr + i
            mode_name = True
            i += 4
        else:
            current.funcs.append((hex(start_addr + i), addr))
            i += 4
    if current != funcs[-1]:
        funcs.append(current)

funcs = []
lut = {}

with open(challenge_path, 'rb') as f:
    f.seek(0x2000)
    raw = f.read()
    parse(raw, 0x804a000, 0x0, funcs, lut)

with open(prompt_mem_dump, 'rb') as f:
    f.seek(4)
    raw = f.read()
    parse(raw, 0x804ac10, 0x804abe8, funcs, lut)

for f in funcs:
    if len(f.funcs) == 1:
        lut[f.funcs[0][1]] = f'{f.name}_1'
        f.funcs[0] = (f.funcs[0][0], f'{f.name}_1')
    else:
        for (idx, sub) in enumerate(f.funcs):
            f.funcs[idx] = (sub[0], lut.get(sub[1], hex(sub[1])))
            if sub[1] < 0x100:
                f.funcs[idx] = (sub[0], f'{f.funcs[idx][1]}\t({chr(sub[1]).encode()})')

with open(output_prog, 'w') as fp:
    fp.write('\n'.join(str(fn) for fn in funcs))

