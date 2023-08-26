import numpy as np
from PIL import Image
from pwn import *
from Crypto.Cipher import AES

# $rax calling aes.NewCipher
key = b"R\375\374\a!\202eO\026?_\017\232b\035r\225f\307M\020\003|M{\273\004\a\321\342\306I"
# $rbx calling aes.NewCBCEncrypter
iv = p64(0x860d1d68d85a8581) + p64(0xcb397916001ee9d1)

def pad(m, block_size = AES.block_size):
    return m + chr(block_size - len(m) % block_size).encode() * (block_size - len(m) % block_size)

def modify(ct_mod):
    ct = b''
    for i, v in enumerate(ct_mod):
        ct += bytes([((i & 0xff) ^ v) & 0xff])
    return ct

def aes_encrypt(filename):
    with open(filename, 'rb') as f:
        pt = f.read()
    pt = pad(pt, AES.block_size)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    intermediate = cipher.encrypt(pt)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct = cipher.encrypt(intermediate)
    return modify(ct)

def aes_decrypt(ct):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    intermediate = cipher.decrypt(pad(ct))
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = cipher.decrypt(pad(intermediate))
    return pt

def decrypt(filename):
    im = Image.open(filename)
    image = np.array(im)
    ct = image[-1]
    ct_bytes = b''.join(bytes([i[0]]) for i in ct).strip(b'\x00')
    cipher_text = modify(ct_bytes)
    return aes_decrypt(modify(ct_bytes))

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print ("ERROR!")
    elif sys.argv[1] == 'e':
        ct = aes_encrypt(sys.argv[2])
        print (ct)
    elif sys.argv[1] == 'd':
        pt = decrypt(sys.argv[2])
        print (pt[:pt.find(b'}') + 1].decode())
    else:
        print ("ERROR!")
