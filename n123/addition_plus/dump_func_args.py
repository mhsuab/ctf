# gdb -x parse.py
import gdb

import sys
sys.path.append('.')
from const import *

flag_base = 0x21

class LogFuncBreakpoint(gdb.Breakpoint):
    FUNC = '(*(int64_t*)($r14 + 0x28)) - $elf_base'
    ARGS = [ '$rdi', '$rsi', '$rdx', '$rcx', '$r8', '$r9', '*(int*)($rsp)', '*(int*)($rsp+8)']

    def stop(self):
        func = gdb.parse_and_eval(self.FUNC)
        args = ', '.join([f'flag_{gdb.parse_and_eval(arg) - flag_base}' for arg in self.ARGS])
        output = f'(*{func})({args})'
        print (output)

gdb.execute(f'file {binary_path}')
gdb.execute(f'starti < <(python3 -c "print (\'\'.join([chr({flag_base} + i) for i in range(0x30)]))")')
# gdb.execute(f'starti < <(python3 -c "print (\'\'.join([\'\'.join([chr({flag_base})] * 7 + [chr({flag_base} + i)]) for i in range(8)]))")')

gdb.execute(f'set $elf_base = $_base("{binary_path}")')
gdb.execute(f'set $calls = $elf_base + {call_node_func_offset}') 
# gdb.execute(f'b *($elf_base + 0x1396)') 
# gdb.execute(f'b *($elf_base + 0x1206)') 
LogFuncBreakpoint('*$calls')

gdb.execute('continue')
# gdb.execute('q')

# break @ 0x1206
# gdb.execute('set *((uint64_t*) ($rsp + 0x40)) = 0x100000000000000')
# gdb.execute('set *((uint64_t*) ($rsp + 0x48)) = 0x1000000000000')
# gdb.execute('set *((uint64_t*) ($rsp + 0x50)) = 0x10000000000')
# gdb.execute('set *((uint64_t*) ($rsp + 0x58)) = 0x100000000')
# gdb.execute('set *((uint64_t*) ($rsp + 0x60)) = 0x1000000')
# gdb.execute('set *((uint64_t*) ($rsp + 0x68)) = 0x10000')
# gdb.execute('set *((uint64_t*) ($rsp + 0x40)) = 0x1')
# gdb.execute('set *((uint64_t*) ($rsp + 0x48)) = 0x100')
# gdb.execute('set *((uint64_t*) ($rsp + 0x50)) = 0x10000')
# gdb.execute('set *((uint64_t*) ($rsp + 0x58)) = 0x1000000')
# gdb.execute('set *((uint64_t*) ($rsp + 0x60)) = 0x100000000')
# gdb.execute('set *((uint64_t*) ($rsp + 0x68)) = 0x10000000000')
# gdb.execute('set *((uint64_t*) ($rsp + 0x40)) = 0x1000000000000')
# gdb.execute('set *((uint64_t*) ($rsp + 0x48)) = 0x100000000000000')

