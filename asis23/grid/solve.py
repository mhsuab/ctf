with open('ct', 'rb') as f:
    ct = f.read()

with open('grids.bin', 'rb') as f:
    grid = f.read()

reverse_table = {
    grid[2 * i + 1]: grid[2 * i] for i in range(255)
}

flag = ''
for (_, c) in zip(range(45), ct):
    flag += chr(reverse_table[c])

print (flag)
