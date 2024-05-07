import re, os
from struct import pack
from subprocess import check_output
from pyda import *

p = process()
BASE = p.maps[p.exe_path].base
PWD = os.path.dirname(p.exe_path)
OUTPUT = os.path.join(PWD, 'ver_pyda')
os.chdir(PWD)

def _decrypt(v, k):
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

def decrypt(checker, key, iteration):
    if os.path.exists(OUTPUT):
        return
    checker = [checker & 0xFFFFFFFF, (checker >> 32)]
    for _ in range(iteration):
        checker = _decrypt(checker, key)
    f = (pack('<L', checker[0]) + pack('<L', checker[1]))
    with open(OUTPUT, 'wb') as fp:
        fp.write(f)

objdump = check_output(f'objdump -M intel -d {p.exe_path}', shell=True).decode()
try:
    res = re.findall(r'mov    ebx,([0-9abcdefx]+)\n', objdump)
    iteration = int(res[0], 16)
except:
    funcname = re.findall(r'call   ([0-9abcdef]+ .*(?<!@plt>))\n', objdump)[0]
    iteration = len(re.findall(re.escape(funcname), objdump))
checker = int(re.findall(r'movabs rax,([0-9abcdefx]+)\n', objdump)[2], 16)
loc = re.findall(r'([0-9abcdef]+):.*call   QWORD PTR.*(?<!@plt>)\n', objdump)[4]

def get_key(p):
    regs = ['rbx', 'r15', 'r14', 'rax']
    key = [p.regs[r] for r in regs]
    decrypt(checker, key, iteration)

p.hook(BASE + int(loc, 16) + 6, get_key)
p.run()
