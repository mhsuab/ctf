from pwn import *

elf = ELF('./breadth.v1')

context.binary = elf
context.terminal = ['tmux', 'splitw', '-v']

gdb_script = '''
b main
r
set $rip=(fcnkKTQpF+32)
ni
x/s $rdi
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

