from snek_decompile import maze_size, target_result, maze_stages, deque

apples = deque()

divisor = maze_size ** 2
for stage in range(len(maze_stages) - 1, -1, -1):
    for apple in maze_stages[stage]:
        cal = apple[0] * maze_size + apple[1]
        if (target_result - cal) % divisor == 0:
            apples.appendleft(apple)
            target_result -= cal
            target_result //= divisor
            target_result ^= 1337
            break

# print (apples)
# deque([(11, 0), (0, 3), (8, 18), (14, 18), (17, 11), (3, 12), (19, 10), (16, 7), (16, 15), (16, 5)])

# (11, 0)     9 L 1 R 2 R 1
# (0, 3)      R 8 R 3 L 3
# (8, 18)     R 5 R 2 L 10 R 6
# (14, 18)    L 1 R 6 R 1
# (17, 11)    7 L 3
# (3, 12)     1 L 4 L 15 L 3
# (19, 10)    2 L 16
# (16, 7)     R 3 R 3
# (16, 15)    R 4 R 2 L 5 L 2 L 1
# (16, 5)     10

cmds = [
    '9 L 1 R 2 R 1',
    'R 8 R 3 L 3',
    'R 5 R 2 L 10 R 6',
    'L 1 R 6 R 1',
    '7 L 3',
    '1 L 4 L 15 L 3',
    '2 L 16',
    'R 3 R 3',
    'R 4 R 2 L 5 L 2 L 1',
    '10'
]

cmd = ' '.join(cmds)

from pwn import *

if args.LOCAL:
    from snek_decompile import game
    if game(cmd):
        log.success('FLAGED')
else:
    r = remote('lac.tf', 31133)
    r.recvuntil(b'snek?')
    r.sendline(cmd.encode())

    try:
        from sys import stdout
        while True:
            stdout.write(r.recv(timeout = 0.5))
            stdout.flush()
    except EOFError:
        pass

# lactf{h4h4_sn3k_g0_brrrrrrrr}

