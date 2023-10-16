import sys
import os

import pickle
mem_file = 'mem.pickle'

if not os.path.exists(mem_file):
    chal = open('chal.txt', 'r').readlines()
    mem = []
    for i in chal:
        mem += [int(c) if c != '' else '' for c in i.split(' ')]
    mem = mem[:-1]
    pickle.dump(mem, open(mem_file, 'wb'))

class Interp:
    def __init__(self):
        self.breakpoints = []
        self.steps_list = []
        self.mute = False
        self.reset('', -1)

    def reset(self, cur_flag, f_idx = 0):
        self.pc = 0
        self.instruction_count = 0
        self.steps_list = []
        self.mem = pickle.load(open(mem_file, 'rb'))
        self.flag = cur_flag
        self.flag_index = f_idx

    def getchar(self):
        if self.flag_index == -1:
            c = sys.stdin.read(1)
            if not self.mute:
                print (c, end='')
        elif self.flag_index == len(self.flag):
            c = '\n'
        else:
            c = self.flag[self.flag_index]
            self.flag_index += 1
        return c

    def get_bignum(self):
        c = self.getchar()
        if c != '%':
            return -(ord(c))
        else:
            # note: all this is just to parse the input as integer/hex
            char_input = '\0'
            result = 0
            c = self.getchar()
            if c == 'x':
                char_input = self.getchar()
                while char_input != '\n':
                    result *= 16
                    # note:
                    # if the input within the hex range
                    # the code is equivalent to the following
                    result += int(char_input, 16)
                    char_input = self.getchar()
                return -result
            else:
                c = ord(c)
                if c > 120 or c == 37 or c < 0x25 or (c - 48) > 9:
                    return -c

                result = c - 48
                char_input = self.getchar()
                while char_input != '\n':
                    result *= 10
                    # note: equivalent if input is a digit
                    result += int(char_input)
                    char_input = self.getchar()
                return -result

    def op1(self, a1, a2):
        bignum = self.get_bignum() if a1 < 0 else self.mem[a1]
        bignum_str = f"get_bignum ({bignum})" if a1 < 0 else f"mem[{a1}] ({bignum})"
        if a2 < 0:
            if not self.mute:
                print (chr(bignum & 0xff), end='')
            self.steps_list.append(f"print {bignum_str};")
        else:
            self.steps_list.append(f"mem[{a2}] -= {bignum_str}; ({self.mem[a2]} -= {bignum})")
            self.mem[a2] -= bignum

    def op2(self ,a1):
        return self.mem[a1] <= 0

    def info(self):
        print (f'pc: {self.pc}')
        print (f'mem[pc: pc + 3]: {self.mem[self.pc: self.pc + 3]}')

        a1 = self.mem[self.pc]
        a2 = self.mem[self.pc + 1]
        a3 = self.mem[self.pc + 2]

        print (f'mem[a1] = {self.mem[a1]} ({chr(self.mem[a1] & 0xff).encode()}, {chr((-self.mem[a1]) & 0xff).encode()})')
        print (f'mem[a2] = {self.mem[a2]} ({chr(self.mem[a2] & 0xff).encode()}, {chr((-self.mem[a2]) & 0xff).encode()})')
        print (f'mem[a3] = {self.mem[a3]}')
        print ()

    def step(self):
        self.steps_list.append(f"@{self.pc:>6}: ")
        self.op1(self.mem[self.pc], self.mem[self.pc + 1])
        if self.op2(self.mem[self.pc + 1]):
            self.steps_list.append(f"jmp {self.mem[self.pc + 2]}\n")
            self.pc = self.mem[self.pc + 2]
        else:
            self.steps_list.append('\n')
            self.pc += 3

    def run(self):
        while self.pc >= 0:
            self.step()
            if self.pc in self.breakpoints:
                print (f'breakpoint at {self.pc}')
                break
            self.instruction_count += 1

    def trace(self, name):
        with open(f'{name}.trace', 'w') as f:
            f.write(''.join(self.steps_list))

    def debug(self):
        prompt = '> '
        while True:
            try:
                cmd = input(prompt).strip().split(' ')
                if cmd[0] == '':
                    cmd = prev_cmd
                if cmd[0] == 'reset':
                    self.reset(cmd[1], 0)
                elif cmd[0] == 'trace':
                    self.trace(cmd[1])
                elif cmd[0] == 'continue' or cmd[0] == 'c':
                    self.run()
                elif cmd[0] == 'run' or cmd[0] == 'r':
                    self.reset(cmd[1], 0)
                    self.run()
                elif cmd[0] == 'step' or cmd[0] == 's':
                    self.step()
                elif cmd[0] == 'info' or cmd[0] == 'i':
                    self.info()
                elif cmd[0] == 'u':
                    self.breakpoints.remove(int(cmd[1]))
                elif cmd[0] == 'b':
                    self.breakpoints.append(int(cmd[1]))
                elif cmd[0] == 'quit' or cmd[0] == 'q':
                    break
                elif cmd[0] == 'eval' or cmd[0] == 'e':
                    c = ' '.join(cmd[1:])
                    print (f'eval: {c}')
                    eval(c)
                elif cmd[0] == 'input':
                    for i in range(16, 80, 8):
                        print (f'{i}: {self.mem[i: i + 8]}')
                elif cmd[0] == 'target':
                    for i in range(98, 162, 8):
                        print (f'{i}: {self.mem[i: i + 8]}')
                else:
                    print ('unknown command')
            except Exception as e:
                print (e)
                break

            prev_cmd = cmd

if __name__ == '__main__':
    inter = Interp()
    inter.debug()
