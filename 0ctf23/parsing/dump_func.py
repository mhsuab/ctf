# gdb -x parse.py
import gdb

import sys
sys.path.append('.')

class LogFuncBreakpoint(gdb.Breakpoint):
    def stop(self):
        print (self.location)

gdb.execute('file ./parser_1e5451a5579d477d7dd2645f30d52a89')

# gdb.execute('set args "flag{dym7GgLb72ID0BPpQVTLRZPAHgjj311er0hu1bKXDWpxCM0B5My5b9g08lXrXugnoQVms69Hf6Af63NvabnOHndrpli}"')
# gdb.execute('set args "flag{000000Lb72ID0BPpQVTLRZPAHgjj311er0hu1bKXDWpxCM0B5My5b9g08lXrXugnoQVms69Hf6Af63NvabnOHndrpli}"')
# gdb.execute('set args "flag{000000Lb72ID0BPpQVTLRZPAHgjv1rwxk_wE1bKXDWpngoBCEBydZQP28lXrXugG3ZVi70UZnSbqdPp2NAB2crMTpli}"')
# gdb.execute('set args "flag{000000Ly7PbxKgm3!8gL!In!3ojao7rJ5YSH7nCg7apLNpHwkwyIt8J5WIXo!_gZLgVIF5IhnmA6vDpzASXocYDIgQi}"')
# gdb.execute('set args "flag{000000Lb72ID0BPpQVTLRZPAHgjv1rwxk_wE1bKXDWpngoBCEBydZQP28lXrXugG3ZVi70UZnSbqdPp2NAB2crMTpli}"')
# gdb.execute('set args "flag{000000Ly7PbxKgm3!8gL!In!3ojdKCr}"')
# gdb.execute('set args "flag{000000LyPxg38JUTqj1jgyJgaxMl_592vW_nQm6H6f3vbOnAQ}"')
gdb.execute('set args "flag{000000Ly7PbxKgm3!8gJXUHTLqjj311j6gSyMJHg7apxCM0lR_y5b9g2cvOW!_gnoQVms69Hf6Af63NvabnOHndAgQi}"')

gdb.execute('start')

gdb.execute('set breakpoint pending on')
gdb.execute('b t_0ctf_parser::eats::eat_remaining')

for i in range(600):
    LogFuncBreakpoint(f'eats::eat_body{i}')
# gdb.execute('b eats::eat_body555')
# gdb.execute('b eats::eat_body0_555')

nodes = ['0', '0_555', '555', '555_14', '14', '14_552', '552', '552_424', '424', '424_385', '385', '385_171', '171', '171_582', '582', '582_69', '69', '69_77', '77', '77_359', '359', '359_17', '17', '17_256',
         '256', '256_534', '534', '534_427', '427', '427_258', '258', '258_329', '329', '329_121', '121', '121_72', '72', '72_198', '198', '198_470', '470', '470_64', '64', '64_3', '3', '3_183', '183', '183_43', '43', '43_573', '573', '573_501',
        '125', '125', '125_412', '412', '412_306', '306', '306_323', '323', '323_250', '250',
        '131_300', '300', '300_10', '10', '10_490', '490', '490_532', '532', '532_554', '554', '82', '82_599', '599']

# for n in nodes:
#     if '_' in n:
#         gdb.execute(f'b t_0ctf_parser::eats::eat_body{n}')
#

gdb.execute('c')
