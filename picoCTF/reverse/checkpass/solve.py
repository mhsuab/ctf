# actual main at 0x5960
# flag format picoCTF{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}
prefix = 'picoCTF{'
suffix = '}'

# addresses, functions to get data needed for decryption
image_base = 0x0
start_key = image_base + 0x39560
end_key = image_base + 0x39960
byte_key = (ida_bytes.get_bytes(start_key, end_key - start_key))

asc_base = image_base + 0x39970
asc = lambda offset, idx: ida_bytes.get_bytes(asc_base + offset + idx, 1)

ct_base = image_base + 0x39D95
ct = ida_bytes.get_bytes(ct_base, 32)

def decrypt(ct, offset):
    '''
    return the original flag that generate the ct with the given offset
    '''
    flag = b''
    intermediate = [b'' for i in range(32)]
    shifted_offset = offset << 8
    asc_current = [ord(asc(shifted_offset, i * 8)) for i in range(32)]
    
    # calculate `intermediate`
    for i in range(32):
        intermediate[asc_current[i]] = ct[i]
    
    # calculate `flag`
    for i in range(32):
        for j in range(256):
            if byte_key[shifted_offset + j] == intermediate[i]:
                flag += bytes([j])
                break
    return flag

def wrap_decrypt(ct):
    for i in range(4):
        ct = decrypt(ct, 3 - i)
    return ct.decode()

def encrypt(flag, offset):
    '''
    flag: bytes
    offset: int
    return bytes
    '''
    shifted_offset = offset << 8
    intermediate = [bytes([byte_key[shifted_offset + flag[i]]]) for i in range(32)]
    return b''.join(intermediate[ord(asc(shifted_offset, i * 8))] for i in range(32))

def wrap_encrypt(flag):
    for i in range(4):
        flag = encrypt(flag, i)
    return flag

# print out the flag
print (prefix + wrap_decrypt(ct) + suffix)