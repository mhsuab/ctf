from dataclasses import dataclass
from os import system, path
from heapq import heappush, heappop
import re
from typing import Dict, List
from subprocess import run

START = 't_0ctf_parser::eats::eat_body0::h41e04f88113bfdc1'
END = 't_0ctf_parser::eats::eat_body599::hebca4204cd765eb9'

EDGE_RE = r".*eat_body(\d+)_(\d+)::"
NODE_RE = r".*eat_body(\d+)::"

def nodename(node):
    return node.split('::')[-2]

def parse_hlil():
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

if not path.exists('graph.dat'):
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

else:

    from ast import literal_eval
    with open('./graph.dat', 'r') as f:
        explored = literal_eval(f.read())

graph = {}

for node in explored:
    if 'eat_body' not in node:
        continue
    graph[node] = []
    queue = list(explored[node])
    while len(queue) > 0:
        next_node = queue.pop(0)
        if 'eat_body' in nodename(next_node):
            graph[node].append(next_node)
        else:
            queue += list(explored[next_node])


func_char = {}
for node in graph:
    for line in funcs[node]:
        if '= nom::bytes::complete::tag::' in line:
            func_char[node] = line.split('"')[1][:1]

node_score = {}

for node in graph:
    overflows = [l for l in funcs[node] if 'add_overflow' in l]
    # print(node, re.match(EDGE_RE, node))
    if re.match(EDGE_RE, node) and '::eat_body0::' not in node and len(overflows) >= 1:
        assert len(overflows) == 1, f'multiple overflows {node} {overflows}'
        assert re.match(r".*\d+_\d+::", node)
        # print("found overflow", node, overflows[0])
        overflow = overflows[0].split(' ')[-1].split(')')[0]
        overflow = int(overflow, 0) - (2**32)
        node_score[node] = overflow
    elif re.match(".*eat_body0::", node):
        node_score[node] = 779
    elif len(overflows) == 0:
        node_score[node] = 0
    else:
        assert len(overflows) == 1, f"multiple overflows {node} {overflows}"
        overflow = overflows[0].split(' ')[-1].split(')')[0]
        overflow = int(overflow, 0)
        subs = [l for l in funcs[node] if '- 0xffff' in l]
        assert(len(subs) == 1)
        sub = int(subs[0].split('- ')[-1], 0) - (2**32)
        print(node, overflow, sub)
        node_score[node] = -sub
        if node_score[node] > 0 and len(graph[node]) > 0:
            assert False, f'wtf {node}, {node_score[node]}, {graph[node]}'

print("-"*80)
node_score = { k: -v for k, v in node_score.items() }
for node, score in node_score.items():
    if re.match(EDGE_RE, node):
        assert score > 0, f'invalid {node} {score}'
    if re.match(NODE_RE, node):
        assert score <= 0, f'invalid {node} {score}'

# print(f'{node_score = }')

# Find the path with the lowest score
best_scores = {START: node_score[START]}
best_paths = {START: [START]}
visited = set()
queue = []
# heappush(queue, (0, start))
queue.append((node_score[START], START))
while len(queue) > 0:
    score, node = queue.pop(0)
    if node in visited:
        continue
    score = best_scores[node]
    for next_node in graph[node]:
        possible_path = best_paths[node] + [next_node]
        possible_score = node_score[next_node] + score
        if next_node not in best_scores or possible_score < best_scores[next_node]:
            if next_node in visited:
                print("wtf improved a node?", next_node)
            best_scores[next_node] = possible_score
            best_paths[next_node] = possible_path
            # heappush(queue, (possible_score, next_node))
            queue.append((possible_score, next_node))

for node in best_scores:
    if len(graph[node]) == 0 and best_scores[node] <= 0:
        print(node, best_scores[node], node_score[node])
        # print(best_paths[node])
        print (''.join(func_char[n] for n in best_paths[node]))


print("-"*80)

# for node in best_scores:
#     if len(graph[node]) == 0:
#         # print(node)
#         # print("\n".join(["\t" + x for x in funcs[node]]))
#         has_faila = ":hed95d41ff956f9bc" in "\n".join(funcs[node])
#         has_failb = ":hca328241dd2a5fa3" in "\n".join(funcs[node])
#         if not (has_faila and has_failb):
#             print(node, f"wtf {node}")

print("-"*80)
END = 't_0ctf_parser::eats::eat_body599::hebca4204cd765eb9'
print(best_scores[END])

print([nodename(n).split('eat_body')[1] for n in best_paths[END]])


# stuff = ''
#
# for node in best_paths[END]:
#     print(node)
#     for line in funcs[node]:
#         if '= nom::bytes::complete::tag::' in line:
#             print(line.split('"')[1][:1])
#             stuff += line.split('"')[1][:1]
#     print()
#
# print(stuff)

print (''.join(func_char[n] for n in best_paths[END]))



@dataclass
class EdgeInfo:
    cost: int
    node: str

@dataclass
class NodeInfo:
    char: str
    cost: int
    edges: Dict[str, List[EdgeInfo]]


lgraph = {}
for node, next in graph.items():
    if re.match(NODE_RE, node):
        new_name = re.match(NODE_RE, node).group(1)
        lgraph[new_name] = NodeInfo(func_char[node], node_score[node], {})
        for n in next:
            assert len(graph[n]) == 1, f'invalid {node} {n} {nn} {graph[n]}'
            for nn in graph[n]:
                tmp = lgraph[new_name].edges.get(func_char[n], [])
                _edge = EdgeInfo(node_score[n], re.match(NODE_RE, nn).group(1))
                tmp.append(_edge)
                lgraph[new_name].edges[func_char[n]] = tmp

# print(lgraph)

pending = { k: 0 for k in lgraph }
for node, info in lgraph.items():
    for edge, edges in info.edges.items():
        for e in edges:
            pending[e.node] += 1
toposort = []
queue = [k for k, v in pending.items() if v == 0]

while len(queue) > 0:
    node = queue.pop(0)
    toposort.append(node)
    for char, edges in lgraph[node].edges.items():
        for edge in edges:
            pending[edge.node] -= 1
            if pending[edge.node] == 0:
                queue.append(edge.node)

print(f'{toposort = }')
cost = dict()
cost["0"] = 0
path = dict()
path["0"] = "L"
fullpath = dict()
fullpath["0"] = ["0 (L)"]
node_path = {'0': ['0']}

for node in toposort:
    for char, edges in lgraph[node].edges.items():
        effective_edge_cost = 0
        effective_edge_path = []
        for edge in edges:
            effective_edge_cost += edge.cost
            effective_edge_cost += lgraph[edge.node].cost
            if len(lgraph[edge.node].edges) > 0 or edge.node == "599":
                node_char = lgraph[edge.node].char
                effective_edge_path += [edge.node + f" ({char}{node_char})"]
                new_cost = cost[node] + effective_edge_cost
                if edge.node not in cost or new_cost < cost[edge.node]:
                    cost[edge.node] = new_cost
                    path[edge.node] = path[node] + char + lgraph[edge.node].char
                    fullpath[edge.node] = fullpath[node] + effective_edge_path
                    node_path[edge.node] = node_path[node].copy()
                    node_path[edge.node].append(edge.node)
                break
            else:
                effective_edge_path += ["*" + edge.node + f" ({char}{node_char})"]

print(f'{len(toposort) = }')
# print(len(cost))
# print(len(path))
# print(len(fullpath))
# print(cost["599"])
print(f'{path["599"] = }')
# print(f'{fullpath["599"] = }')
print(f'{node_path["599"] = }')

backtraces = ['171', '289', '505', '72', '180', '38', '125', '472', '306', '367', '339', '131', '277', '238', '548', '482']
print (f'{backtraces = }')
print (f'{best_paths[END]}')


count = 0
for n in fullpath['599']:
    for b in backtraces:
        if n.startswith(b + ' '):
            print ('back', b, n)
            count += 1
print (f'{count = }, {len(backtraces) = }')

# print(node_score)

dot_nodes = [
    (re.match(NODE_RE, k).group(1), node_score[k], k)
    for k in graph if re.match(NODE_RE, k)
]

dot_edges = [
    (re.match(NODE_RE, k).group(1), re.match(EDGE_RE, v).group(2), node_score[v], func_char[v], v)
    for k in graph if re.match(NODE_RE, k)
    for v in graph[k] if re.match(EDGE_RE, v)
]

with open('graph.dot', 'w') as f:
    f.write('digraph G {\n')
    for node in dot_nodes:
        used = node[2] in best_paths[END]
        # used = node[0] in path_node['599']
        # f.write(f'\t"{node[0]}" [label="n{node[0]}$\n{node[1]}" color="{ "red" if used else "black" }" penwidth="{ 3 if used else 1 }"];\n')
        f.write(f'\t"{node[0]}" [label="{node[0]}" color="black" penwidth="1"];\n')
    for edge in dot_edges:
        orig_edge_name = f""
        used = edge[4] in best_paths[END]
        # f.write(f'\t"{edge[0]}" -> "{edge[1]}" [label="{edge[2]}\n{edge[3]}" color="{ "red" if used else "black" }" penwidth="{ 3 if used else 1 }"];\n')
        f.write(f'\t"{edge[0]}" -> "{edge[1]}" [label="{edge[2]}\n{edge[3]}" color="black" penwidth="1"];\n')
        # if used:
        #     f.write(f'\t"{edge[0]}" [label="{edge[0]}" color="red" penwidth="3"];\n')
        #     print(edge[3], edge[2])
    f.write('}\n')

flag = f'flag{{000000{path["599"]}}}'
system('dot -Tsvg graph.dot -o graph.svg')
print(f'{flag = }')
print (' '.join(['./parser_1e5451a5579d477d7dd2645f30d52a89', f'flag{{000000{path["599"]}}}']))
run(['./parser_1e5451a5579d477d7dd2645f30d52a89', flag])
