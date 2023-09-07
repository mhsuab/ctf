with open('cipher.txt', 'r') as f:
    ct = f.read()

key = 'CYLAB'
flag = ''

i, j = 0, 0
while (i) < len(ct):
    c = ord(ct[i])
    if c >= 0x41 and c <= 0x5a:
        c = c - ord(key[j])
        c = c % 26
        c += 0x41
        j += 1
    elif c >= 0x61 and c <= 0x7a:
        c = c - ord(key[j]) - 0x20
        c = c % 26
        c += 0x61
        j += 1
    flag += chr(c)
    i += 1
    j = j % 5

print (flag)