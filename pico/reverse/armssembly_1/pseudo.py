def func1(x):
    a, b, c = 85, 6, 3
    d = a << b
    d = d // c
    d = d - x
    return (d == 0)

# True if argument == ((a << b) // c)
ans = (85 << 6) // 3
print (ans, f'{ans:08x}'[-8:])
