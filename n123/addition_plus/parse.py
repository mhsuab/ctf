func = [0x15b0, 0xbc90, 0x14200, 0x1d4c0, 0x28120, 0x33390, 0x39f50, 0x436c0]

with open('./addition_plus.bndb_disassembly.asm', 'r') as f:
    asms = f.readlines()

d = {}
key = ''

for line in asms:
    if 'sub_' in line:
        key = line[line.find('sub'):line.find('(')]
        d[key] = []
    elif key == '':
        pass
    elif line.startswith('//'):
        pass
    elif line == '\n':
        pass
    else:
        d[key].append(line[29:].strip())
        if 'retn' in line:
            key = ''

with open('disasm.asm', 'w') as f:
    for key in func:
        k = f'sub_{key:x}'
        f.write(f'{k}\n')
        f.write('\n'.join(d[k]))
        f.write('\n\n')

