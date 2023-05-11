from pwn import *

elf = ELF('./not-crypto')

context.binary = elf
context.terminal = ['tmux', 'splitw', '-v']

gdb_script = '''
b memcmp
c
x/s $rdi
'''

def conn():
    r = process([elf.path])
    gdb.attach(r, gdb_script)
    return r

def solve(r):
    r.recvuntil(b'?\n')
    r.sendline(b'a' * 0x40)
    r.interactive()

if __name__ == '__main__':
    r = conn()
    solve(r)
    r.close()

