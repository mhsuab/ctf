from collections import defaultdict
from dataclasses import dataclass
import os
import re
from typing import Dict, List, Tuple

START = 't_0ctf_parser::eats::eat_body0::h41e04f88113bfdc1'
END = 't_0ctf_parser::eats::eat_body599::hebca4204cd765eb9'

EDGE_RE = r".*eat_body(\d+)_(\d+)::"
NODE_RE = r".*eat_body(\d+)::"

@dataclass
class EdgeInfo:
    char: str
    cost: int
    nodes: Tuple['NodeInfo', 'NodeInfo']

@dataclass
class NodeInfo:
    char: str
    cost: int
    edges: Dict[str, List[EdgeInfo]]

def nodename(node):
    return node.split('::')[-2]

def parse_hlil():
    '''
    Construct function call graph from High Level IL
    '''
    with open('./parser_1e5451a5579d477d7dd2645f30d52a89.bndb_hlil.txt', 'r') as f:
        hlil = f.read()
    
    pieces = hlil.split('\n\n')
    pieces = [p.strip() for p in pieces if p.strip() != '']

    func2save = ['eat_body', 'nom::', '::parse::', '::call_mut::', 'eat_tail', 'die']
    func_starts = [i for i, p in enumerate(pieces) if p.count('\n') == 0 and '(' in p and p.endswith(')')]
    
    funcs = {}
    for i in func_starts:
        func_name_possibilities = pieces[i].replace('(', ' ').split(' ')
        func_name_possibilities = [p for p in func_name_possibilities if len(p) > 0]
        func_name_possibilities = [p for p in func_name_possibilities if '::' in p or p.startswith('sub_')]
        if len(func_name_possibilities) != 1:
            continue
        func_name = func_name_possibilities[0]
        if not any(x in func_name for x in func2save):
            continue
        funcs[func_name] = pieces[i+1].split('\n')

    return funcs

funcs = parse_hlil()

# load graph
if os.path.exists('graph.dat'):
    from ast import literal_eval
    with open('./graph.dat', 'r') as f:
        explored = literal_eval(f.read())
else:
    dot_edges = []
    explored = {}
    queue = [START]

    while len(queue) > 0:
        print('>>>>>>>', len(queue), len(funcs), len(explored))
        node = queue.pop(0)
        if node in explored:
            continue
        explored[node] = []
        for line in funcs[node]:
            for func in funcs.keys():
                if func in line:
                    explored[node].append(func)
                    queue.append(func)

    with open('./graph.dat', 'w') as f:
        f.write(repr(explored))

def get_add_overflow(node):
    pass


# extract the graph with only remaining functions with `eat_body`
graph = defaultdict(list)
extract = 'eat_body'
for node in explored:
    if extract not in node:
        continue
    _node = nodename(node)
    queue = list(explored[node])
    while queue:
        next_node = queue.pop(0)
        _next_node = nodename(next_node)
        if extract in _next_node:
            graph[_node].append(_next_node)
        elif _next_node == 'eat_tail' or _next_node == 'die':
            if _next_node == 'die':
                print (re.match(EDGE_RE, node))
                print (re.match(NODE_RE, node))
            graph[_node].append(_next_node)
        else:
            queue += list(explored[next_node])

# print (f'{graph["eat_body5"] = }')
# print (f'{graph["eat_body336_599"] = }')
# print (f'{graph["0"] = }')

# nodes: Dict[int | Tuple[int, int], NodeInfo | EdgeInfo] = {}
# nodes2explored = [ START ]
# if nodes2explored:
#     node = nodes2explored.pop(0)
#     print (explored[START])
#     parsed = re.match(NODE_RE, START)
#     print (parsed.group(1))
#     parsed = re.match(EDGE_RE, START)
#     print (parsed)

print (graph)
print (f'{graph["eat_body5"] = }')
print (f'{graph["eat_body599"] = }')

print (graph['die'])
print (graph['eat_tail'])

dot_nodes = [
    # (re.match(NODE_RE, k).group(1) if re.match(NODE_RE, k) is not None else nodename(k)) # , node_score[k], k)
    k.replace('eat_body', '')
    for k in graph if k.count('_') <= 1
]
print (dot_nodes)

dot_edges = [
    (k.replace('eat_body', ''), v.replace('eat_body', '').split('_')[1]) # , node_score[v], func_char[v], v)
    for k in graph if k.count('_') <= 1
    for v in graph[k] if v.count('_') == 2
]
dot_edges.extend([
    (k.replace('eat_body', ''), v + '_' + k.replace('eat_body', '')) # , node_score[v], func_char[v], v)
    for k in graph if k.count('_') <= 1
    for v in graph[k] if v == 'die' or v == 'eat_tail'
])

with open('graph_s.dot', 'w') as f:
    f.write('digraph G {\n')
    for node in dot_nodes:
        # used = node[2] in best_paths[END]
        # used = node[0] in path_node['599']
        # f.write(f'\t"{node[0]}" [label="n{node[0]}$\n{node[1]}" color="{ "red" if used else "black" }" penwidth="{ 3 if used else 1 }"];\n')
        f.write(f'\t"{node[0]}" [label="{node[0]}" color="black" penwidth="1"];\n')
    for edge in dot_edges:
        orig_edge_name = f""
        # used = edge[4] in best_paths[END]
        # f.write(f'\t"{edge[0]}" -> "{edge[1]}" [label="{edge[2]}\n{edge[3]}" color="{ "red" if used else "black" }" penwidth="{ 3 if used else 1 }"];\n')
        f.write(f'\t"{edge[0]}" -> "{edge[1]}" [color="black" penwidth="1"];\n')
        # if used:
        #     f.write(f'\t"{edge[0]}" [label="{edge[0]}" color="red" penwidth="3"];\n')
        #     print(edge[3], edge[2])
    f.write('}\n')

os.system('dot -Tsvg graph_s.dot -o graph_s.svg')
















