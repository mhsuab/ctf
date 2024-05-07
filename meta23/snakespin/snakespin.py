#!/usr/bin/env python3

def check_flag(flag):
    if len(flag) % 2 != 0:
        return False
    flag = bytearray(flag)
    for i in range(0, len(flag), 2):
        flag[i], flag[i+1] = flag[i+1], flag[i]
    for i in range(len(flag)):
        flag[i] += i
    return flag.hex() == '654e63775848814d716b69727a807970837675727d847583888e807a8e8c917e86829688a19e'

flag = input('Enter the flag: ').encode()

if check_flag(flag):
    print("That's it!")
else:
    print("Not quite...")
