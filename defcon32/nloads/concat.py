from glob import glob
s = 'ver_pyda'

results = {}
for f in glob(f'output/**/{s}'):
    results[f] = open(f, 'rb').read()

flag = b''
for i in range(13613):
    flag += results.get(f'output/{i}/{s}', b'\x00' * 8)

with open('flag.jpeg', 'wb') as f:
    f.write(flag)
