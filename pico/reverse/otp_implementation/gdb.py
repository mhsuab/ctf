import gdb
# gdb -q -x gdb.py

gdb.execute('file ./otp')
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