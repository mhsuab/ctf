def encode(flag):
    return ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

def decode(enc):
    flag = ''
    for i in enc:
        h = '{:04x}'.format(ord(i))
        flag += chr(int(h[:2], 16)) + chr(int(h[2:], 16))
    return flag

if __name__ == '__main__':
    with open('enc', 'r') as f:
        print (decode(f.read()))