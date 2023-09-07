# FLAG: `PICOCTF{These are the access codes to the vault: 1063340}`

def gen_key(num, digit):
    # function `sub_407AF0`
    v5 = pow(2, digit * 4) - 1
    v3 = pow((num & (num ^ v5)) + 37, 7)
    v4 = 0
    if (v3 >= 9.223372036854776e18):
        v3 -= 9.223372036854776e18
        if (v3 < 9.223372036854776e18):
            v4 = 0x8000000000000000
    return (v4 + v3) / (((v4 + v3) >> 8) % 0x1E240)

def gernerate(number):
    _input = str(number)
    return 16 * (int(gen_key(int(_input[0]), len(_input))) >> 2)

print (f'The key is: {gernerate(3):d}')
print (f'The key is: {gernerate(100):d}')
print (f'The key is: {gernerate(1):d}')