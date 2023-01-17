from pwn import *

elf = ELF('./keygenme')

context.binary = elf
context.terminal = ['tmux', 'splitw', '-v']

gdb_script = '''
set breakpoint pending on
b *0x0000555555555419
r < <(echo "A")
x/s ($rbp-0x30)
'''

def conn():
    r = process([elf.path])
    gdb.attach(r, gdb_script)
    return r

def solve(r):
    r.interactive()

if __name__ == '__main__':
    r = conn()
    solve(r)
    r.close()

