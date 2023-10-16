import subprocess

IN = 'output.py'
OUT = 'output'

flag = list(input("input flag: "))
flag = flag[6:-1]
flag = list(flag)

def convertify(flag):
    print (f'{flag = }')
    INPUT = ""
    LENGTH = ""
    for c in flag:
        print (c)
        INPUT = "[L_" + c + "[N" + INPUT
        LENGTH += "]]"
    return "_: E[E[Z]] = QRW_s29[L___TAPE_END__[N" + INPUT + "[MR[N[L___TAPE_END__[N[E[E[Z]]]]]]]]]" + LENGTH + "()"

with open("output.py", 'r') as file:
    lines = file.readlines()
lines[461] = convertify(flag)
with open(OUT, 'w') as file:
    file.writelines(lines)

with subprocess.Popen(["mypy", OUT]) as mypy:
    success = mypy.wait(timeout=10)
if success == 0:
    print("correct!")
else:
    print("incorrect!")
