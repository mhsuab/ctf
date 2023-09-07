x, y, z = 1, 1, 0

def lose():
    print("You were eaten by a grue.")
    exit(1)

def win():
    print("Congratulations, you made it!")
    exit(0)

def add_z():
    z += 1

def sub_z():
    z -= 1

possible_value = {'X': lose, 'Y': win, '+': add_z, '-': sub_z}
matrix = [[0 for _ in range(0x10)] for _ in range(0x10)]    # load from file (0174 ~ 0574)
'''
order from file to matrix
matrix[0][0]
matrix[1][0]
matrix[2][0]
...
matrix[15][0]
matrix[0][1]
matrix[1][1]
matrix[2][1]
...
matrix[15][1]
...
matrix[15][15]
'''

def evaluate(x, y, z):
    possible_value[matrix[x][y]]()

if __name__ == '__main__':
    print("Welcome to the M A T R I X\nCan you make it out alive?")
    path = input()

    while True:
        c = path[0]
        path = path[1:]

        if c == 'u':
            y += 1
        elif c == 'd':
            y -= 1
        elif c == 'l':
            x -= 1
        elif c == 'r':
            x += 1
        else:
            lose()

        idx = x + 0x10 * y # matrix = 0x16 x 0x16
        evaluate(x, y, z)