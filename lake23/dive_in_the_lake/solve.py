# 00000024 0000000000000007 0000000000000008 DW_OP_const1u: 1; DW_OP_breg5 (rdi): 0; DW_OP_breg4 (rsi): 0; DW_OP_and; DW_OP_breg1 (rdx): 0; DW_OP_and; DW_OP_const8u: 7219272754963824708; DW_OP_ne; DW_OP_bra: 3; DW_OP_const1u: 3; DW_OP_mul; DW_OP_const8u: 9259542123273814144; DW_OP_dup; DW_OP_dup; DW_OP_breg5 (rdi): 0; DW_OP_and; DW_OP_const1u: 0; DW_OP_ne; DW_OP_bra: 26; DW_OP_breg4 (rsi): 0; DW_OP_and; DW_OP_bra: 9; DW_OP_breg1 (rdx): 0; DW_OP_and; DW_OP_bra: 3; DW_OP_const1u: 3; DW_OP_mul; DW_OP_breg5 (rdi): 0; DW_OP_dup; DW_OP_mul; DW_OP_breg4 (rsi): 0; DW_OP_dup; DW_OP_mul; DW_OP_plus; DW_OP_const8u: 18116903027530606121; DW_OP_ne; DW_OP_bra: 3; DW_OP_const1u: 3; DW_OP_mul; DW_OP_breg1 (rdx): 0; DW_OP_dup; DW_OP_mul; DW_OP_breg4 (rsi): 0; DW_OP_dup; DW_OP_mul; DW_OP_plus; DW_OP_const8u: 16612709672999228116; DW_OP_ne; DW_OP_bra: 3; DW_OP_const1u: 7; DW_OP_mul; DW_OP_const1u: 189; DW_OP_eq; DW_OP_stack_value
#
# a = 0 # rdi
# b = 0 # rsi
# c = 0 #rdx
#
# val = 1
# if (a & b & c == 7219272754963824708):
#     val *= 3
#
# if (a & 9259542123273814144 == 0):
#     if (b & 9259542123273814144 == 0):
#         if (c & 9259542123273814144 == 0):
#             val *= 3
# if ((a**2 + b**2) == 18116903027530606121):
#     val *= 3
# if ((b**2 + c**2) == 16612709672999228116):
#     val *= 7
# if val == 189:
#     print("success")
#     flag = 1

from cvc5.pythonic import *
a, b, c = BitVecs('a b c', 64)
val = BitVecs('v', 64)
args = [a, b, c]

const = 9259542123273814144

s = Solver()

s.add((a & b & c) == 7219272754963824708)
s.add((a & const) == 0)
s.add((b & const) == 0)
s.add((c & const) == 0)

s.add((a * a + b * b) == 18116903027530606121)
s.add((c * c + b * b) == 16612709672999228116)

if s.check() == sat:
    model = s.model()
    print (b''.join([model[i].as_long().to_bytes(8, 'little') for i in args]))

