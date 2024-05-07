flag = bytearray.fromhex('654e63775848814d716b69727a807970837675727d847583888e807a8e8c917e86829688a19e')
for i in range(len(flag)):
    flag[i] -= i
for i in range(0, len(flag), 2):
    flag[i], flag[i+1] = flag[i+1], flag[i]
print (flag.decode())
