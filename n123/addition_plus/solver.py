from cvc5.pythonic import *
from tqdm import tqdm

debug = False

length = 0x30
func = [0x15b0, 0xbc90, 0x14200, 0x1d4c0, 0x28120, 0x33390, 0x39f50, 0x436c0]
target = b"\x29\x41\xf0\xd7\x47\x1a\x24\xab\xb8\x23\x86\x00\xf3\x5a\x2b\x5d\x03\xbf\xe5\xaf\x26\x0b\x91\x22\x21\x8c\xd9\x68\xad\x4a\x08\x2f\x24\xd7\x12\x55\xf2\x34\xca\x28\x83\xf2\xd3\xca\x54\xd1\xc6\x36"

with open('disasm.asm', 'r') as f:
    prog = [[line.split() for line in _func.split('\n')] for _func in f.read().split('\n\n')]
prog = {int(lines[0][0][4:], 16): lines[1:] for lines in prog if lines[0] != []}

flag = [ BitVec(f'flag_{i}', 8) for i in range(length) ]
calc = [ 0 for _ in range(length) ]

reg2key = {
    'rdi': 'rdi',
    'edi': 'rdi',
    'rsi': 'rsi',
    'esi': 'rsi',
    'rdx': 'rdx',
    'edx': 'rdx',
    'rcx': 'rcx',
    'ecx': 'rcx',
    'r8': 'r8',
    'r8d': 'r8',
    'r9': 'r9',
    'r9d': 'r9',
    'rsp': 'rsp',
    'ebp': 'rbp',
    'rbp': 'rbp',
    'ebx': 'rbx',
    'rbx': 'rbx',
    'r10d': 'r10',
    'r10': 'r10',
    'r11d': 'r11',
    'r11': 'r11',
    'r12d': 'r12',
    'r12': 'r12',
    'r13d': 'r13',
    'r13': 'r13',
    'eax': 'rax',
    'rax': 'rax',
}

def eval_right(var, mapping, frame):
    ret = 0
    match_pair = (var[0][0], var[0])
    match match_pair:
        case ('[', _):
            left, right = (var[0][1:-1]).split('+')
            assert left == right, f'{left = } != {right = }'
            left = mapping[reg2key[left]]
            right = mapping[reg2key[right]]
            ret = left * 2
        case (_, 'dword'):
            left, right = (var[1][1:-1]).split('+')
            assert left == 'rsp', f'Register in dword mem access not rsp but {left}'
            ret = mapping[int(right, 16) // 8 - frame]
        case _:
            ret = mapping[reg2key[var[0]]]
    return ret

def calculate(prog, mapping):
    frame = 1
    for line in tqdm(prog):
        if debug: print (line)
        match line[0]:
            case 'push':
                frame += 1
            case 'lea':
                lhs = line[1][:-1]
                mapping[reg2key[lhs]] = eval_right(line[2:], mapping, frame)
                if debug: print (mapping[reg2key[lhs]])
            case 'mov':
                lhs = line[1][:-1]
                mapping[reg2key[lhs]] = eval_right(line[2:], mapping, frame)
                if debug: print (mapping[reg2key[lhs]])
            case 'and':
                lhs_key = reg2key[line[1][:-1]]
                lhs = mapping[lhs_key]
                rhs = mapping[reg2key[line[2]]]
                if debug: print (f'{lhs = }, {rhs = }')
                mapping[lhs_key] = ((lhs) & rhs)
                if debug: print (mapping[lhs_key])
            case 'xor':
                lhs_key = reg2key[line[1][:-1]]
                lhs = mapping[lhs_key]
                rhs = mapping[reg2key[line[2]]]
                if debug: print (f'{lhs = }, {rhs = }')
                mapping[lhs_key] = lhs ^ rhs
                if debug: print (mapping[lhs_key])
            case 'add':
                lhs_key = reg2key[line[1][:-1]]
                lhs = mapping[lhs_key]
                rhs = mapping[reg2key[line[2]]]
                if debug: print (f'{lhs = }, {rhs = }')
                mapping[lhs_key] = lhs ^ rhs
                if debug: print (mapping[lhs_key])
            case 'endbr64':
                pass
            case 'retn':
                break
            case 'pop':
                # TODO?
                pass
            case _:
                if debug: print (line)
                break
        if debug: input()
    return mapping['rax']

for i in range(6):
    start = 8 * i
    for j in range(8):
        mapping = {
            'rdi': flag[start],
            'rsi': flag[start + 1],
            'rdx': flag[start + 2],
            'rcx': flag[start + 3],
            'r8': flag[start + 4],
            'r9': flag[start + 5],
            0: flag[start + 6],
            1: flag[start + 7],
        }
        calc[start + j] = calculate(prog[func[j]], mapping)
    break

s = Solver()
for i in range(8):
    s.add(flag[i] > 32 , flag[i] < 127, calc[i] == target[i])

if s.check() == sat:
    m = s.model()
    print (''.join([chr(m[flag[i]].as_long()) for i in range(length)]))
else:
    print ('unsat')

