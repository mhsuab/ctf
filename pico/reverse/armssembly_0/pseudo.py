arg0 = 1765227561
arg1 = 1830628817

def func1(x0, x1):
    if x0 <= x1:
        return x1
    return x0

ans = func1(arg0, arg1)
print (ans, f'{ans:08x}'[-8:])
