from os import system

commands = open('commands', 'rb').read()
table = commands[0x0174:0x0574]
cells = [table[i:i + 4] for i in range(0, len(table), 4)]

for i in range(len(cells)):
    if cells[i] == b'\x81\xfb\x000':
        cells[i] = '.'
    elif cells[i] == b'\x81\x85\x050':
        cells[i] = 'Y'
    elif cells[i] == b'0\x00\x00\x00':
        cells[i] = '0'
    elif cells[i] == b'\x81t\x050':
        cells[i] = '-'
    elif cells[i] == b'\x81\x7f\x050':
        cells[i] = '+'

def display(x, y, commands):
    print (x, y, commands)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == y and j == x:
                if matrix[i][j] == '.' or (matrix[i][j] == '-' and z <= 0):
                    print ("invalid")
                    c = commands[-1]
                    commands = commands[:-1]
                    if c == 'r':
                        x -= 1
                    elif c == 'l':
                        x += 1
                    elif c == 'u':
                        y += 1
                    elif c == 'd':
                        y -= 1
                    input('press any key to resume...')
                    return False, x, y, commands
                print ('X', end='')
            else:
                print (matrix[i][j], end='')
        print ()
    return True, x, y, commands

matrix = [cells[i:i + 16] for i in range(0, 256, 16)]
x, y, z = 1, 1, 0
commands = ''
ignored = False
while True:
    system('clear')
    print ('[MATRIX]')
    ret, x, y, commands = display(x, y, commands)
    if not ret:
        continue
    if matrix[y][x] == '+':
        z += 1
    elif matrix[y][x] == '-':
        z -= 1
    else:
        pass
    print ('commands: ', commands)
    print ('z:', z)
    c = input()
    if c == 'r':
        x += 1
    elif c == 'l':
        x -= 1
    elif c == 'u':
        y -= 1
    elif c == 'd':
        y += 1
    else:
        print ('invalid')
        continue
    commands += c
    if matrix[y][x] == 'Y':
        break

print ("WIN!")
print ("commands: ", commands)