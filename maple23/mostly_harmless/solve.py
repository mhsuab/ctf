from dataclasses import dataclass

@dataclass
class element:
    next: int
    char: str

with open('./src/output.py', 'r') as f:
    raw = f.readlines()

data = dict(map(
    lambda s: (
        int(s[10:12]),
        element(int(s[37:39]), s[27])
    ),
    raw[320:460:2]
))

cur = 29
flag = ''
while cur != 71:
    flag += data[cur].char
    cur = data[cur].next

print (f'maple{{{flag}}}')
