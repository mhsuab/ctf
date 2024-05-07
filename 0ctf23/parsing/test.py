from pwn import *

elf = ELF('./parser_1e5451a5579d477d7dd2645f30d52a89')

START = 't_0ctf_parser::eats::eat_body0::h41e04f88113bfdc1'
END = 't_0ctf_parser::eats::eat_body599::hebca4204cd765eb9'

EDGE_RE = r".*eat_body(\d+)_(\d+)::"
NODE_RE = r".*eat_body(\d+)::"

def nodename(node):
    return node.split('::')[-2]


