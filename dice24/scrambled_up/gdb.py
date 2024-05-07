# gdb -x gdb.py
import gdb

filename = 'scrambled-up'

import sys
sys.path.append('.')

class ClearBreakpoint(gdb.Breakpoint):
    def stop(self):
        gdb.execute('set *(int*)$rdi = 0')
        gdb.execute('set *(int*)$rsi = 0')
        return False

before_getline = f'$_base("{filename}")+0x4f288'

gdb.execute(f'file {filename}')
gdb.execute('start')

ClearBreakpoint(f'*{gdb.parse_and_eval(before_getline)}')
gdb.execute(f'b *({gdb.parse_and_eval(before_getline)} + 0x5)')

gdb.execute('c')
