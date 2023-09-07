ct = b'\xc5u\x95\xa5\x81\x80\xf3D\xf1\x994\x81:_P\x93g\xee\x12\x0c\x15:\xda\x1coP\x80Ic\xf26\xd3\x93dFc\x84\xb5:Z\x9c>@\xf5\x19 \x7f\x08\x00H\n\x03'

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

R = [c for c in b'picoCTF{']
A = [i for i in range(0x100)]

# function @0x10080
'''
...
remu            a4, a3, a2
lbu             a7, 0(a6)
addi            a6, a6, 1
addi            a3, a3, 1
add             a4, a4, a1
lbu             a4, 0(a4)
addw            a4, a4, a7
addw            a5, a5, a4
andi            a4, a5, 0FFh
add             a4, a4, a0
lbu             t1, 0(a4)
andi            a5, a5, 0FFh
sb              t1, -1(a6)
sb              a7, 0(a4)
bne             a3, t3, loc_1009E
'''
j = 0
for i in range(0x100):
    j = (j + R[i % 8] + A[i]) & 0xff
    A[i], A[j] = A[j], A[i]

# function @0x100D2
'''
sub_100D2:
lbu             a4, 256(A)
lbu             a5, 257(A)
addiw           a4, a4, 1
andi            a4, a4, 255
sb              a4, 256(A)
add             a4, a4, A
lbu             a2, 0(a4)
addw            a5, a5, a2
andi            a5, a5, 255
sb              a5, 257(A)
add             a5, a5, A
lbu             a1, 0(a5)
addw            a3, a2, a1
sb              a1, 0(a4)
andi            a4, a3, 255
sb              a2, 0(a5)
add             A, A, a4
lbu             A, 0(A)
ret
'''
x = 0
y = 0
flag = ''
for i in range(len(ct)):
    x = (x + 1) & 0xff
    y = (y + A[x]) & 0xff
    A[x], A[y] = A[y], A[x]
    flag += chr(A[(A[x] + A[y]) & 0xff] ^ ct[i])

print (flag)
