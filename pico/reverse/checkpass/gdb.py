import gdb
# gdb -q -x gdb.py
breakpoints = [0x555555405cf8, 0x555555405d15, 0x555555405d32, 0x555555405d42, 0x555555405d60, 0x555555405d71, 0x555555405d8f, 0x555555405da0, 0x555555405dbe, 0x555555405dcf, 0x555555405dec, 0x555555405dfc, 0x555555405e18, 0x555555405e28, 0x555555405e45, 0x555555405e55, 0x555555405e72, 0x555555405e82, 0x555555405e9f, 0x555555405eaf, 0x555555405ecc, 0x555555405edc, 0x555555405efc, 0x555555405f0c, 0x555555405f2c, 0x555555405f3c, 0x555555405f5c, 0x555555405f6c, 0x555555405f8c, 0x555555405f9c, 0x555555405fbc, 0x555555405fcc, 0x555555405fec, 0x555555405ffc, 0x55555540601c, 0x55555540602c, 0x55555540604c, 0x55555540605c, 0x55555540607c, 0x55555540608c, 0x5555554060ac, 0x5555554060bc, 0x5555554060dc, 0x5555554060ec, 0x55555540610c, 0x55555540611c, 0x55555540613c, 0x55555540614c, 0x55555540616c, 0x55555540617c, 0x55555540619c, 0x5555554061ac, 0x5555554061cc, 0x5555554061dc, 0x5555554061fc, 0x55555540620c, 0x55555540622c, 0x55555540623c, 0x55555540625c, 0x55555540626c, 0x55555540628c, 0x55555540629c, 0x5555554062b8, 0x5555554062c8]
print (len(breakpoints))

gdb.execute('file ./checkpass')
gdb.execute('b strncmp')

def search():
    flag_length = 100
    pos = '0123456789abcdef'
    charptr = gdb.lookup_type('char').pointer()
    key = ''
    prev = len(key)
    while True:
        for c in pos:
            print ((key + c).ljust(flag_length, '0'))
            gdb.execute(f'r {(key + c).ljust(flag_length, "0")}')
            rdi = gdb.parse_and_eval ("$rdi")
            rsi = gdb.parse_and_eval ("$rsi")
            exp = (rsi + prev).cast(charptr).dereference()
            enc = (rdi + prev).cast(charptr).dereference()
            if exp == enc:
                prev += 1
                key += c
                break
        if len(key) == 100:
            print (key)
            break

search()