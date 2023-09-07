from pwn import *

with open('switcheroo', 'rb') as f:
    f.seek(0x203c)
    length = 0x243b - 0x203c + 1
    ct = f.read(length)


flag = b''
for i in range(0x3f):
    _start = 0x107
    while _start != -1:
        _start = ct.find(bytes([i]), _start + 1)
        to_check = 7 - (_start % 8)

        pt = -1
        if to_check != 0 and ct[_start + to_check] >= to_check:
            # to_check == 0: JUMP to `0x040106b`
            # ct[_start + to_check] >= to_check
            #   => s.t. it can check till `i` and jump to `0x40106e`
            pt = _start - 7 + to_check

        if pt != -1 and pt % 8 == 0:
            pt = pt // 8
            if pt >= 0x21 and pt <= 0x7e:
                flag += bytes([pt])
                break

log.success(f'FLAG: {flag.decode()}')

if args.VERIFY:
    elf = ELF('./switcheroo')
    context.binary = elf
    r = process([elf.path])
    r.recvuntil(b'flag: ')
    r.sendline(flag)
    log.info(r.recvline()[:-1].decode())
