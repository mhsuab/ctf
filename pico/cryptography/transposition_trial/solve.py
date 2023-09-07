with open('message.txt', 'r') as f:
    ct = f.read()

flag = ''

for i in range(0, len(ct), 3):
    flag += (ct[i + 2] + ct[i:i + 2])

print (flag)