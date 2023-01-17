'''
modify one bit in `game` to display every things in the stage
find flag display in ascii art on the side

picoCTF{ur_4_w1z4rd_8F4B04AE}
'''

stages = []
with open('game', 'rb') as f:
    f.seek(0x119840)
    for _ in range(10):
        stages.append(f.read(10000))
        f.read(16)

for idx in range(10):
    print ('\n'.join((stages[idx].decode())[i:i + 100] for i in range(0, 10000, 100)), end='\n\n')
