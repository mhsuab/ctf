prog = './chal.forth'

values_address = 0x804bb9c
lut_address = 0x804bc54

with open(prog, 'r') as f:
    challenge = {int(line.split()[0], 16): line.split()[1:] for line in f.readlines()[:-1] if line != '\n'}

# Get values to match from file
values = []
offset = 0
while True:
    val = challenge.get(values_address + offset, [''])[0]
    if val.startswith('fn_'):
        break
    else:
        values.append(val)
    offset += 4

# Get the lookup table
lut = {}
idx = 0
while True:
    val = challenge.get(lut_address + 4 * idx, [''])[0]
    if val.startswith('fn_'):
        break
    else:
        lut[val] = idx
    idx += 1

flag = []
for v in values:
    flag.append(chr(lut[v]))
print (''.join(flag))

