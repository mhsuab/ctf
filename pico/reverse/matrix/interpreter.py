class sim:
    def __init__(self, filename = '', input_buf = b''):
        self.stack = []
        self.mem = []
        self.getc_count = 0
        self.commands = open(filename, 'rb').read()
        self.pc = 0
        self.input_buf = input_buf
        self.breakpoints = []

    def debugger(self):
        while True:
            try:
                command = input('> ').split()
                if (len(command) == 0):
                    command = ['step']
                elif command[0] == 'q' or command[0] == 'quit':
                    break
                exec(f'self.{command[0]}({", ".join(c.__repr__() for c in command[1:])})')
                if (command[0] == 'step'):
                    self.info()
            except KeyboardInterrupt:
                exit()
            except Exception as e:
                print (f'$pc @{self.pc:04x}')
                print (e)

    def __get_stack(self, idx):
        try:
            return f"{self.stack[idx]:04x}"
        except:
            return ''

    def __get_mem(self, idx):
        try:
            return f"{self.mem[idx]:04x}"
        except:
            return ''

    def __get_breakpoints(self):
        if len(self.breakpoints) == 0:
            print ('No Breakpoints')
            return
        print ('[Breakpoints]')
        print ('\tidx\taddress')
        for idx, pc in enumerate(self.breakpoints):
            print (f'\t{idx}\t@{pc}({hex(pc)})')
        print ()

    def info(self, sub = ''):
        if sub == 'b':
            self.__get_breakpoints()
            return
        print ('\n[Instructions]')
        print ('$pc -> \t', end='')
        idx = self.__dis(self.pc)
        for _ in range(3):
            print ('\t', end='')
            idx = self.__dis(idx)

        print (f'\nstack->{self.__get_stack(0):<20}mem->{self.__get_mem(0)}')
        for i in range(1, min(max(len(self.stack), len(self.mem)), 20)):
            print (f'       {self.__get_stack(i):<25}{self.__get_mem(i)}')
        if max(len(self.stack), len(self.mem)) > 10:
            print (f'{"....":>11}{"....":>25}')

    def b(self, pc):
        if isinstance(pc, str):
            if pc.startswith('0x'):
                pc = int(pc[2:], 16)
            else:
                pc = int(pc)
        self.breakpoints.append(pc)

    def run(self, input_buffer = b''):
        self.stack = []
        self.mem = []
        self.getc_count = 0
        self.pc = 0
        if self.input_buf != b'' and input_buffer != b'':
            self.input_buf = input_buffer
        self.c()

    def c(self):
        while True:
            if self.step():
                break

            if self.pc in self.breakpoints:
                self.info()
                break
        return False

    def step(self):
        inst = self.commands[self.pc]
        self.pc += 1

        if inst == 0x0:
            pass
        elif inst == 0x1:
            print (f'[exit with code {self.stack.pop()}]')
            return True
        elif inst == 0x10:
            self.stack.append(self.stack[-1])
        elif inst == 0x11:
            self.stack.pop()
        elif inst == 0x12:
            self.stack[-2] += self.stack[-1]
            self.stack.pop()
        elif inst == 0x13:
            self.stack[-2] -= self.stack[-1]
            self.stack.pop()
        elif inst == 0x14:
            self.stack[-2], self.stack[-1] = self.stack[-1], self.stack[-2]
        elif inst == 0x20:
            self.mem.append(self.stack.pop())
        elif inst == 0x21:
            self.stack.append(self.mem.pop())
        elif inst == 0x30:
            self.pc = self.stack.pop()
        elif inst == 0x31:
            dest = self.stack.pop()
            cond = (self.stack.pop() == 0)
            if (cond):
                self.pc = dest
        elif inst == 0x32:
            dest = self.stack.pop()
            cond = (self.stack.pop() == 0)
            if not cond:
                self.pc = dest
        elif inst == 0x33:
            dest = self.stack.pop()
            cond = (self.stack.pop() < 0)
            if cond:
                self.pc = dest
        elif inst == 0x34:
            dest = self.stack.pop()
            cond = (self.stack.pop() <= 0)
            if cond:
                self.pc = dest
        elif inst == 0xc0:
            if self.input_buf == b'':
                self.input_buf = input().encode()
            self.stack.append(self.input_buf[0])
            self.input_buf = self.input_buf[1:]
            self.getc_count += 1
        elif inst == 0xc1:
            word = self.stack.pop()
            print (int.to_bytes(word, 2, 'little').decode(), end='')
        elif inst == 0x80:
            word = self.commands[self.pc]
            self.stack.append(word)
            self.pc += 1
        elif inst == 0x81:
            word = int.from_bytes(self.commands[self.pc: self.pc + 2], 'little')
            self.stack.append(word)
            self.pc += 2
        return False

    def __dis(self, idx):
        inst = self.commands[idx]
        print (f'{idx:04x}: ', end='')
        idx += 1

        if inst == 0x0:
            print ('nop')
        elif inst == 0x1:
            print ('end')
        elif inst == 0x10:
            print ('copy')
        elif inst == 0x11:
            print ('pop')
        elif inst == 0x12:
            print ('add')
        elif inst == 0x13:
            print ('sub')
        elif inst == 0x14:
            print ('swap')
        elif inst == 0x20:
            print ('store')
        elif inst == 0x21:
            print ('load')
        elif inst == 0x30:
            print ('jmp')
        elif inst == 0x31:
            print ('jz')
        elif inst == 0x32:
            print ('jnz')
        elif inst == 0x33:
            print ('jl')
        elif inst == 0x34:
            print ('jle')
        elif inst == 0xc0:
            print ('getc')
        elif inst == 0xc1:
            print ('putc')
        elif inst == 0x80:
            word = self.commands[idx:idx + 1]
            print (f'pushw {word[0]:04x} ({word.__repr__()[2:-1]})')
            idx += 1
        elif inst == 0x81:
            word = int.from_bytes(self.commands[idx: idx + 2], 'little')
            print (f'pusha {word:04x}')
            idx += 2
        return idx

    def disassemble(self, idx = 0, inst_count = -1):
        if inst_count == -1:
            while idx < len(self.commands):
                idx = self.__dis(idx)
        for _ in range(inst_count):
            idx = self.__dis(idx)

if __name__ == '__main__':
    path = b'rrrrrlrlrlrlrllddddddlddrrddrrrrdddrruuuruuuuuuurrddddddddlddrd'
    s = sim(filename='commands', input_buf=path)
    s.debugger()
