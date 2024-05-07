'''
tcp stream 6
unzip -P bbd7e42689ce9bdef9dfb9aa2c78d4fd script.zip

tcp stream 7
content of script.zip

tcp stream 8
content of flag.png (encrypted with `exfil.py`)
'''

def rand():
    s = 53
    while True:
        yield s
        s = (1337 * s + 2600) % 8080 * 256 // 8080

gen = rand()

with open('flag.png.enc', 'r') as f:
    r = f.read().replace('\n', '')

r = bytes.fromhex(r)
pt = [b ^ next(gen) for b in r]

with open('flag.png', 'wb') as f:
    f.write(bytes(pt))
