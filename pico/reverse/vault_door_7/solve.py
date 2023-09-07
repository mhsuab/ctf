from pwn import *

x = [
    1096770097,
    1952395366,
    1600270708,
    1601398833,
    1716808014,
    1734293296,
    842413104,
    1684157793,
]
flag = [p32(i, endian = 'big').decode() for i in x]

print (f"picoCTF{{{''.join(flag)}}}")