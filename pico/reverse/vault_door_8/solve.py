excepted = [
    0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4,
    0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86,
    0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xD2,
    0xD0, 0xB4, 0xE1, 0xC1, 0xE0, 0xD0, 0xD0, 0xE0
]

def switchBits(c, p1, p2):
    _c = [i for i in f'{c:08b}'[::-1]]
    _c[p1], _c[p2] = _c[p2], _c[p1]
    return int(''.join(_c[::-1]), 2)

def unscramble(c):
    c = switchBits(c, 6, 7)
    c = switchBits(c, 2, 5)
    c = switchBits(c, 3, 4)
    c = switchBits(c, 0, 1)
    c = switchBits(c, 4, 7)
    c = switchBits(c, 5, 6)
    c = switchBits(c, 0, 3)
    c = switchBits(c, 1, 2)
    return c

flag = [chr(unscramble(c)) for c in excepted]

print (f"picoCTF{{{''.join(flag)}}}")