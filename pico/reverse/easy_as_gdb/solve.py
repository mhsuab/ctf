import gdb
# gdb -q -x solve.py

gdb.execute('file ./brute')
gdb.execute('b *0x565559aa')

def search():
    flag_length = 30
    pos = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefpio{}'
    intptr = gdb.lookup_type('int').pointer()
    flag = ''
    prev = len(flag)
    while True:
        for c in pos:
            print (flag+c)
            gdb.execute(f'r <<< {flag}{c}')
            idx = gdb.parse_and_eval ("$ebp-0x14")
            val = idx.cast(intptr).dereference()
            if val > prev:
                flag = flag + c
                prev = val
                break
        if prev == 30:
            print (flag)
            break

search()
