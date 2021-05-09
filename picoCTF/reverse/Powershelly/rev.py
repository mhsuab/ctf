OUTPUT_PATH = 'output.txt'

def rev_scamble(b, seed):
    raw2 = bin(b)[2:]
    bm = [raw2[i:i + 2] for i in range(0, len(raw2), 2)]
    raw = ['' for i in range(len(bm))]
    for i in range(len(bm)):
        y = (i * seed) % len(bm)
        n = bm[y]
        while (n == '10'):
            y = (y + 1) % len(bm)
            n = bm[y]
        if n == '11':
            raw[i] = '1'
        else:
            raw[i] = '0'
        bm[y] = '10'
    raw = ''.join(raw)
    return [raw[i:i + 6] for i in range(0, len(raw), 6)]

def rev():
    total = 264

    blocks = [0 for _ in range(total)]
    result = 0
    seeds = [((i * 127) % 500) for i in range(1, total + 1)]
    randoms = [((((i * 327) % 681 ) + 344) % 313) for i in range(1, total + 1)]
    with open(OUTPUT_PATH, 'r') as f:
        results = [int(i) for i in f.read().split()]
    blocks = []
    for i in range(len(results)):
        fun = result ^ randoms[i] ^ results[i]
        result = results[i]
        blocks += [rev_scamble(fun, seeds[i])]
    return '\r\n'.join([' '.join(i[j] for i in blocks) for j in range(len(blocks[0]))])

if __name__ == '__main__':
    with open('input.txt', 'w') as f:
        f.write(rev() + '\r\n')