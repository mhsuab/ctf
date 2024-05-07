import socket
import sys

def rand():
    s = 53
    while True:
        yield s
        s = (1337 * s + 2600) % 8080 * 256 // 8080

gen = rand()

if len(sys.argv) != 4:
    print("Usage: script.py <host> <port> <file_path>")
    sys.exit(1)

host = sys.argv[1]
port = sys.argv[2]
file_path = sys.argv[3]

with open(file_path, "rb") as f:
    d = f.read()

d = [format(i^next(gen), '02x') for i in d]

s = socket.socket()
s.connect((host, int(port)))

for i in range(len(d)//32+1):
    s.sendall(("".join(d[i*32:i*32+32]) + "\n").encode())

s.close()