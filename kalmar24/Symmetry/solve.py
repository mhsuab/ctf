from constants import *
from typing import Dict, List, Tuple
from pwn import *

HOST = 'chal-kalmarc.tf'
PORT = 8
BINARY = ELF('./challenge')

def get_nibbles(t, idx):
    return t[idx]
def get_val_from_lut(shift, b):
    return lut[shift][b]
def mod_nibbles(mod: List, idx, nibble):
    if (nibble & 0xf == nibble) or idx % 2 == 0:
        mod[idx] = nibble & 0xf
    else:
        mod[idx] = nibble & 0xf
        mod[idx - 1] = (mod[idx - 1] + (nibble & 0xf0) // 0x10) & 0xf
def rev_box(box: List, val) -> int:
    return box.index(val)
def rev_get_val_from_lut(val, idx) -> int:
    for i in range(16):
        l = lut[i]
        if val == (l[idx] & 0xf):
            return i
    raise Exception(f"unable to find corresponding value, {val}")

def rev_block(shift, pt, key, intermediate):
    text = [c for c in pt]
    for j in range(15, -1, -1):
        box = [-1 for _ in range(16)]
        for k in range(16):
            box[shuffle_index[k]] = get_val_from_lut(shift[j], k)
        for ii in range(16):
            intermediate[ii] = rev_box(box, rev_box(box, text[ii]))
        for n in range(16):
            intermediate[n] = rev_get_val_from_lut(intermediate[n], get_nibbles(key, n))
        for m in range(16):
            text[m] = intermediate[box[m]]
    return text

# NOTE: `rev` part
print ("=== REV ===")
flag = b''
stack = [0 for _ in range(0x20)]
for (shift, text, key) in zip(shifts, ciphertexts, keys):
    text = rev_block(shift, text, key, stack)
    flag += p64(int(''.join(f'{c:x}' for c in text), 16), endian = 'big')
print (flag.strip(b'\x00').decode())

# NOTE: `crypto` part
class Crypt:
    def __init__(self, shift_options, key, text_options) -> None:
        self.table: Dict[int, int] = {}
        self.shift_options: List[int] = shift_options
        self.key: List[int] = key
        self.text_options: List[int] = text_options
        self.nmemb: int = len(self.shift_options) * len(self.text_options)
        self.__stack: List[int] = [-1 for _ in range(0x90)] + [ord(i) for i in 'kalmar{fake_flag_for_testing_:)}'] + [0 for _ in range(0x100)]
        self.__gen()

    def __gen(self):
        m = [0, 0]
        for i in range(0x100):
            mod_nibbles(m, 0, i)
            mod_nibbles(m, 1, i)
            s = ''.join(f'{j:x}' for j in m)
            assert s not in self.table, f'result, {s}, in dictionary already'
            self.table[0x10 * m[0] + m[1]] = i

    def __get_box(self, mem):
        return self.__stack[0x10 + mem]
    def __set_box(self, mem, val):
        self.__stack[0x10 + mem] = val

    def __symulate(self, shifts, pts) -> Tuple[List[int], List[int]]:
        def sym(shift, text) -> Tuple[int, bytes]:
            fidx = -1
            text = [c for c in text]
            for j in range(16):
                for k in range(16):
                    self.__set_box(shuffle_index[k], get_val_from_lut(shift[j], k))
                for m in range(16):
                    assert self.__get_box(m) >= 0, "access uninitialized memory"
                    mod_nibbles(self.__stack, self.__get_box(m), get_nibbles(text, m))
                for n in range(16):
                    nibble = get_val_from_lut(get_nibbles(self.__stack, n), get_nibbles(self.key, n))
                    mod_nibbles(self.__stack, n, nibble & 0xf)
                for ii in range(16):
                    leak = self.__get_box(get_nibbles(self.__stack, ii))
                    val = self.__get_box(leak)
                    assert leak >= 0, f"access uninitialized memory, box[{get_nibbles(self.__stack, ii) + 0x10:02x}] = {leak:02x}"
                    assert val >= 0, f"access uninitialized memory, box[{leak:02x}] = {val:02x}"
        
                    mod_nibbles(text, ii, val)
                    if leak > 0x10:
                        if fidx == -1:
                            fidx = (leak - 0x80)
                        assert fidx == (leak - 0x80), f'access different character from the flag, 0x{fidx:x} != (0x{leak:x} - 0x80)'
            assert fidx != -1, 'flag_idx not found'
            return fidx, bytes(text[:16])

        flag_indices, texts = [], []
        for i in range(self.nmemb):
            fidx, text = sym(shifts[i], pts[i])
            flag_indices.append(fidx)
            texts.append(0x10 * text[0] + text[1])

        return flag_indices, texts

    def __binary(self, r: remote | process, shifts: List[List[int]], texts: List[List[int]]) -> List[int]:
        result =[]
        r.sendlineafter(b'Number of blocks: ', str(self.nmemb).encode())
        for i in range(self.nmemb):
            r.sendlineafter(f'key for block {i}: '.encode(), ''.join(f'{c:x}' for c in self.key).encode())
            for (j, s) in enumerate(shifts[i]):
                r.sendlineafter(f'shift {j} for block {i}: '.encode(), (f'{s:x}').encode())
            r.sendlineafter(f'plaintext for block {i}: '.encode(), ''.join(f'{t:x}' for t in texts[i]).encode())
        r.recvuntil(b'Ciphertexts:\n')
        for i in range(self.nmemb):
            r.recvuntil(f'Block {i}: '.encode())
            c = int(r.recv(2), 16)
            result.append(c)
        return result

    def solve(self) -> bytes:
        flag: List[bytes] = [b'?' for _ in range(0x20)]
        shifts = []
        texts = []
        for offset in self.shift_options:
            for i in self.text_options:
                shifts.append([*[0 for _ in range(15)], offset])
                texts.append([i for _ in range(0x10)])

        if args.EXPLOIT:
            r = remote(HOST, PORT)
        else:
            r = process([BINARY.path])

        indices, cts = self.__symulate(shifts, texts)
        if not args.SYM:
            cts = self.__binary(r, shifts, texts)

        for (fidx, c) in zip(indices, cts):
            flag[fidx] = self.table[c].to_bytes(length=1, byteorder='little')

        if not args.SYM:
            r.close()

        return b''.join(flag)

print ("=== CRYPTO ===")

flag = Crypt(
    shift_options = [0x80, 0x90],
    key = [0] * 16,
    text_options = [i for i in range(0x10)][::-1],
).solve().decode()
print (flag)
