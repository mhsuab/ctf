with open('rev_this', 'r') as f:
    raw = f.read()

flag = raw[:8]

for i in range(8, 23):
    if (i & 1) != 0:
        flag += chr(ord(raw[i]) + 2)
    else:
        flag += chr(ord(raw[i]) - 5)

flag += '}'
print (flag)