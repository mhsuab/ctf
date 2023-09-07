flag = ['' for _ in range(32)]
target2match = 'jU5t_a_sna_3lpm12g94c_u_4_m7ra41'

for i in range(8):
    flag[i] = target2match[i]

for i in range(8, 16):
    flag[23 - i] = target2match[i]

for i in range(16, 32, 2):
    flag[46 - i] = target2match[i]

for i in range(31, 16, -2):
    flag[i] = target2match[i]

print (f"picoCTF{{{''.join(flag)}}}")