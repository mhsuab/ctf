myBytes = [
    '106', '85', '53', '116', '95', '52', '95', '98',
    '0x55', '0x6e', '0x43', '0x68', '0x5f', '0x30', '0x66', '0x5f',
    '0142', '0131', '0164', '063 ', '0163', '0137', '0146', '064',
    'a' , '8' , 'c' , 'd' , '8' , 'f' , '7' , 'e' ,
]
flag = ''

for i in myBytes:
    if len(i) == 1 and i in '0123456789abcdef':
        flag += i
    elif i[:2] == '0x':
        flag += chr(int(i[2:], 16))
    elif i[0] == '0':
        flag += chr(int(i[1:], 8))
    else:
        flag += chr(int(i))

print (f"picoCTF{{{flag}}}")