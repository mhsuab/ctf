from os import system

def nodename(node):
    return node.split('::')[-2]


with open('./parser_1e5451a5579d477d7dd2645f30d52a89.bndb_hlil.txt', 'r') as f:
    hlil = f.read()


pieces = hlil.split('\n\n')
pieces = [p.strip() for p in pieces if p.strip() != '']

func_starts = [i for i, p in enumerate(pieces) if p.count('\n') == 0 and '(' in p and p.endswith(')')]

funcs = {}
for i in func_starts:
    func_name_possibilities = pieces[i].replace('(', ' ').split(' ')
    func_name_possibilities = [p for p in func_name_possibilities if len(p) > 0]
    func_name_possibilities = [p for p in func_name_possibilities if '::' in p or p.startswith('sub_')]
    if len(func_name_possibilities) != 1:
        # print(f'wtf {pieces[i]}')
        continue
    func_name = func_name_possibilities[0]
    if not any(x in func_name for x in ['eat_body', 'nom::', '::parse::', '::call_mut::']):
        continue
    funcs[func_name] = pieces[i+1].split('\n')


start = 't_0ctf_parser::eats::eat_body0::h41e04f88113bfdc1'
# start = 't_0ctf_parser::eats::eat_body0_291::h7983c3e18c877c54'


if False:
# if True:

    dot_edges = []
    explored = {}
    queue = [start]

    while len(queue) > 0:
        print('>>>>>>>', len(queue), len(funcs), len(explored))
        node = queue.pop(0)
        if node in explored:
            continue
        # explored[node] = set()
        explored[node] = []
        for line in funcs[node]:
            # print(line)
            for func in funcs.keys():
                if func in line:
                    # print(f'{node} -> {func}')
                    # explored[node].add(func)
                    explored[node].append(func)
                    # dot_edges.append((node, func))
                    queue.append(func)

        # dot_edges = list(set(dot_edges))




    graph = {}

    for node in explored:
        if 'eat_body' not in node:
            continue
        graph[node] = set()
        queue = list(explored[node])
        while len(queue) > 0:
            next_node = queue.pop(0)
            if 'eat_body' in next_node:
                graph[node].add(next_node)
            else:
                queue += list(explored[next_node])

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
        # graph[node] = set()
        graph[node] = []
        queue = list(explored[node])
        while len(queue) > 0:
            next_node = queue.pop(0)
            if 'eat_body' in nodename(next_node):
                # graph[node].add(next_node)
                graph[node].append(next_node)
            else:
                queue += list(explored[next_node])

# dot_edges = [(k, v) for k in graph for v in graph[k]]

# with open('graph.dot', 'w') as f:
#     f.write('digraph G {\n')
#     for edge in dot_edges:
#         f.write(f'\t"{edge[0]}" -> "{edge[1]}";\n')
#     f.write('}\n')

# system('dot -Tsvg graph.dot -o graph.svg')
# print('done writing graph.svg')

func_char = {}
for node in graph:
    for line in funcs[node]:
        if '= nom::bytes::complete::tag::' in line:
            func_char[node] = line.split('"')[1][:1]


new_graph = {}

for (node, nexts) in graph.items():
    current = []
    new_graph[node] = []
    for n in nexts:
        c = func_char[n]

        if c not in current:
            new_graph[node].append([n.split('::')[-2][8:]])
            current.append(c)
        else:
            # new_graph[node].append()
            new_graph[node][current.index(c)].append(n.split('::')[-2][8:])

        # if c not in current:
        #     new_graph[node].append(n)
        #     current.append(c)
        # else:
        #     print (f'{node = }, {n = }, {new_graph[node][current.index(c)]}, {c = }')

print ('new graph')
backtraces = []
for (k, v) in new_graph.items():
    for n in v:
        if len(n) > 1:
            print (k.split('::')[-2][8:], n)
            backtraces.append(k.split('::')[-2][8:])
print ('new graph end')
print (f'{backtraces = }')

node_score = {}

for node in graph:
    overflows = [l for l in funcs[node] if 'add_overflow' in l]
    if '::eat_body0::' not in node and len(overflows) >= 1:
        assert len(overflows) == 1, f'wtf {node} {overflows}'
        overflow = overflows[0].split(' ')[-1].split(')')[0]
        overflow = int(overflow, 0) - (2**32)
        node_score[node] = overflow
    else:
        node_score[node] = 0

# Find the path with the lowest score
best_scores = {start: node_score[start]}
best_paths = {start: [start]}
queue = [start]
while len(queue) > 0:
    node = queue.pop(0)
    for next_node in graph[node]:
        possible_path = best_paths[node] + [next_node]
        possible_score = sum([node_score[n] for n in possible_path])
        if next_node not in best_scores or possible_score > best_scores[next_node]:
            best_scores[next_node] = possible_score
            best_paths[next_node] = possible_path
            queue.append(next_node)


LAST = 't_0ctf_parser::eats::eat_body599::hebca4204cd765eb9'

print('last', [nodename(n).split('eat_body')[1] for n in best_paths[LAST]])


# stuff = ''
#
# for node in best_paths[LAST]:
#     print(node)
#     for line in funcs[node]:
#         if '= nom::bytes::complete::tag::' in line:
#             print(line.split('"')[1][:1])
#             stuff += line.split('"')[1][:1]
#     print()
#
# print(stuff)

print ('flag: ', ''.join(func_char[n] for n in best_paths[LAST]))

ans = 0
for n in best_paths[LAST]:
    ans += node_score[n]
print ('ans', ans + 779)
# print (ans + 14)
