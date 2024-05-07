from string import printable
ct = [122, 126, 115, 37, 97, 100, 105, 99, 109, 84, 107, 88, 95, 72, 90, 5, 97, 53, 32, 74, 95, 76, 94, 117, 44, 49, 110, 91, 54, 29, 95, 53, 20, 17, 76, 54, 8, 51, 26, 119, 84, 105, 60, 71, 47, 102, 120, 74, 70, 114, 12, 124, 124, 81, 120, 123, 90, 33, 10, 63, 69, 97, 35, 119, 46, 99, 103, 109, 74]

lut = {}
alt = {'.': 'array_int_input_by_append.txt', '/': 'slash'}
for c in printable:
    try:
        with open('./dumps/' + c if c != '.' and c != '/' else alt[c], 'r') as f:
            lut[c] = [int(i) for i in f.readlines()]
    except:
        lut[c] = [0 for _ in range(69)]

flag = ['' for _ in range(69)]
for (i, t) in enumerate(ct):
    for c in printable:
        if t == lut[c][i]:
            flag[i] = c
print (''.join(flag))
