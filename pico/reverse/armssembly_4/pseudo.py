arg = 3964545182

def func1(x):
    print ('func1')
    if x <= 100:
        return func3(x)
    x += 100
    return func2(x)

def func2(x):
    print ('func2')
    if x > 499:
        x += 13
        return func5(x)
    x -= 86
    return func4(x)

def func3(x):
    print ('func3')
    return func7(x)

def func4(x):
    print ('func4')
    func1(17)
    return x

def func5(x):
    print ('func5')
    return func8(x)

def func7(x):
    print ('func7')
    if x <= 100:
        return 7
    return x

def func8(x):
    print ('func8')
    return x + 2

ans = func1(arg)
print (ans, f'{ans:08x}'[-8:])
