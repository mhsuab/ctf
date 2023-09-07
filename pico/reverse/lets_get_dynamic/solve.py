from pwn import *

elf = ELF('./chall')

context.binary = elf
context.terminal = ['tmux', 'splitw', '-v']

gdb_script = '''
b memcmp
r < <(echo "A")
p (char*)$rsi
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

