from typing import List, Tuple
from bot import machineRule1, GHOST, PLAYER, EMPTY

from pwn import *
context.terminal = ['tmux', 'splitw', '-h']

ghost_dialog_list = [b'OoooOOOoooo', b'Booooo-hoooo',b'Eeeeek',b'Hoooowl',
    b'Sliiither',b'Waaail',b'Woooosh',b'Eeeerie',b'Creeeeeeak',
    b'Haauuunt',b'Woooo-woooo',b'Gaaaasp',b'Shiiivver',
]

def next(board: List[List[str]]) -> Tuple[int, int, int]:
    i, j = machineRule1(PLAYER, board)
    index = 3 * (i % 3) + (j % 3) + 1
    return i, j, index

def shuffle_lut(game: int, turn: int, rand_number: int):
    array_len = 13
    lut = [i for i in range(array_len)]
    seed = game ^ rand_number ^ turn
    modulo = array_len - 1

    for i in range(modulo):
        lut[seed % (array_len - i)], lut[modulo - i] = lut[modulo - i], lut[seed % (array_len - i)]
    
    return lut

def get_ghost_loc(game: int, turn: int, rand_number: int, resp: bytes) -> Tuple[int, int]:
    lut = shuffle_lut(game, turn, rand_number)
    ret = lut.index(ghost_dialog_list.index(resp))
    return (ret // 3), (ret % 3)

def print_game(board):
    print ('\n---+---+---\n'.join(' ' + (' | '.join(b for b in row)) for row in board))

prompt = b'Spell: '
gdbscript = '''
b *(0x28db + $_base("ghost_no_flag"))
b *(0x25ac + $_base("ghost_no_flag"))
set $game = 0x5555555590e0 - 0x0000555555554000 + $_base("ghost_no_flag")
'''

host, port = 'flu.xxx', 10140

r = remote(host, port)
# r = process(['./ghost_no_flag', '10', '32'])
r.recvline()
r.recvline()
r.recvuntil(b'|  ')
num = r.recvline()[:-1]
print (num)
rand_number = int(num)
print (f'{rand_number = }')

for game in range(50):
    board = [[EMPTY for _ in range(3)] for _ in range(3)]

    for turn in range(9):
        print (f'{game = }; {turn = }')
        if game % 2 == turn % 2:
            r.recvuntil(prompt)
            i, j, index = next(board)
            board[i][j] = PLAYER
            r.sendline(str(index).encode())

            while b'S' == r.recv(1):
                board[i][j] = EMPTY
                i, j, index = next(board)
                board[i][j] = PLAYER
                r.sendline(str(index).encode())
        
        else:
            r.recvuntil(b'*')
            resp = r.recvuntil(b'*', drop=True)
            i, j = get_ghost_loc(game, turn, rand_number, resp)
            board[i][j] = GHOST

        if b'(' == r.recv(1):
            print ('ROUND', r.recvuntil(b')', drop = True).decode())
            break

        print_game(board)

    os.system('clear')

r.recvuntil(b'! ')
print (r.recvuntil(b'}').decode())

