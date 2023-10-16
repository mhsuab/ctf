'''
try brute force the flag with instruction count
'''
from interp import Interp

prefix = 'hitcon{'

from string import printable

interp = Interp()
interp.mute = True

max_count = 0
max_char = ''
second_max_count = 0
for c in printable:
    interp.reset(prefix + c, 0)
    interp.run()
    if interp.instruction_count > max_count:
        second_max_count = max_count
        max_count = interp.instruction_count
        max_char = c
    elif interp.instruction_count > second_max_count:
        second_max_count = interp.instruction_count
    print (f'{c}: {interp.instruction_count}')

print ()
print (f'max_char: {max_char}')
print (f'max_count: {max_count}')
print (f'second_max_count: {second_max_count}')
print (f'diff: {max_count - second_max_count}')

prefix += max_char

max_count = 0
max_char = ''
second_max_count = 0
for c in printable:
    interp.reset(prefix + c, 0)
    interp.run()
    if interp.instruction_count > max_count:
        second_max_count = max_count
        max_count = interp.instruction_count
        max_char = c
    elif interp.instruction_count > second_max_count:
        second_max_count = interp.instruction_count
    print (f'{c}: {interp.instruction_count}')

print ()
print (f'max_char: {max_char.encode()}')
print (f'max_count: {max_count}')
print (f'second_max_count: {second_max_count}')
print (f'diff: {max_count - second_max_count}')
