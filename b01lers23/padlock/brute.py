# just avoid actually reversing the obfuscated code
# and start brute forcing the challenge

from pwn import *
from string import printable
printable = printable[:-4].encode()

elf = ELF('./quine')

context.binary = elf

def conn(flag):
    return process([elf.path, flag])

flag = b''

while True:
    for c in printable:
        c = chr(c).encode()
        if c == '\t':
            print ("ERROR")
            exit()

        r = conn(flag + c)
        result = r.recvline()[2:-1]
        r.close()
        if result[-1] == 79: # b'O'
            flag += c
            break
        print (flag + c)
    print (flag)
    if flag[-1] == 125: # b'}'
        break
print (flag.decode())