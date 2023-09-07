from pwn import *

host = 'mercury.picoctf.net'
port = 35862

def calc_password():
    key = '''0x18439f28:     0x38    0x36    0x31    0x38    0x33    0x36    0x66    0x31
    0x18439f30:     0x33    0x65    0x33    0x64    0x36    0x32    0x37    0x64
    0x18439f38:     0x66    0x61    0x33    0x37    0x35    0x62    0x64    0x62
    0x18439f40:     0x38    0x33    0x38    0x39    0x32    0x31    0x34    0x65'''
    cmp = '''0x18439f48:     0x4a    0x53    0x47    0x5d    0x41    0x45    0x03    0x54
    0x18439f50:     0x5d    0x02    0x5a    0x0a    0x53    0x57    0x45    0x0d
    0x18439f58:     0x05    0x00    0x5d    0x55    0x54    0x10    0x01    0x0e
    0x18439f60:     0x41    0x55    0x57    0x4b    0x45    0x50    0x46    0x01'''

    key = [word for word in key.split() if ':' not in word]
    cmp = [word for word in cmp.split() if ':' not in word]

    password = ''
    for i, j in zip(key, cmp):
        password += chr(int(i, 16) ^ int(j, 16))
    return password

def hash_lookup():
    key = "861836f13e3d627dfa375bdb8389214e"
    return 'goldfish'

def conn():
    return remote(host, port)

def solve(r):
    r.recvuntil(b'Enter Password: ')
    r.sendline(calc_password())
    r.recvuntil(b'?\n')
    r.sendline(hash_lookup())
    r.recvuntil(b'Flag is:  ')
    print (r.recvline()[:-1].decode())

if __name__ == '__main__':
    r = conn()
    solve(r)
    r.close()
