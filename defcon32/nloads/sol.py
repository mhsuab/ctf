import gdb, re
from struct import pack
from subprocess import check_output

i = arg0

def decrypt(v, k):
    MASK = 0xFFFFFFFF
    delta = 0x9E3779B9
    s = (delta * 32) & MASK
    v0 = v[0]
    v1 = v[1]
    for _ in range(32):
        v1 -= ((((v0<<4) & MASK) + k[2]) & MASK) ^ ((v0 + s) & MASK) ^ ((((v0>>5) & MASK) + k[3]) & MASK)
        v1 &= MASK
        v0 -= ((((v1<<4) & MASK) + k[0]) & MASK) ^ ((v1 + s) & MASK) ^ ((((v1>>5) & MASK) + k[1]) & MASK)
        v0 &= MASK
        s = (s-delta) & MASK
    return [v0, v1]

filename = f'output/{i}/beatme'
objdump = check_output(f'objdump -M intel -d ./output/{i}/beatme', shell=True).decode()
try:
    res = re.findall(r'mov    ebx,([0-9abcdefx]+)\n', objdump)
    iteration = int(res[0], 16)
except:
    funcname = re.findall(r'call   ([0-9abcdef]+ .*(?<!@plt>))\n', objdump)[0]
    iteration = len(re.findall(re.escape(funcname), objdump))
checker = int(re.findall(r'movabs rax,([0-9abcdefx]+)\n', objdump)[2], 16)
loc = re.findall(r'([0-9abcdef]+):.*call   QWORD PTR.*(?<!@plt>)\n', objdump)[4]

gdb.execute('gef config context.enable 0')
gdb.execute(f'set cwd output/{i}')
gdb.execute(f'file {filename}')
gdb.execute('set breakpoint pending on')
gdb.execute('start < <(echo "aaaaaaaa")')
gdb.execute(f'b *($_base("{filename}")+0x{loc}+6)')
gdb.execute('c')

key_loc = ['$rbx', '$r15', '$r14', '$rax']
key = [gdb.parse_and_eval(reg).__int__() for reg in key_loc]

checker = [checker & 0xFFFFFFFF, (checker >> 32)]
for _ in range(iteration):
    checker = decrypt(checker, key)
f = (pack('<L', checker[0]) + pack('<L', checker[1]))
with open(f'output/{i}/ver6', 'wb') as fp:
    fp.write(f)
gdb.execute('q')
