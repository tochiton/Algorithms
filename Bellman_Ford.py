import sys
a_graph = {
    'A': [('B', -1), ('C', 4)],
    'B': [('D', 1), ('C', 3), ('E', 2)],
    'C': [],
    'D': [('B', 2), ('C', 5)],
    'E': [('D', -3)],
}

data_set_1 = {
    'A': [('B', 4), ('H', 8)],
    'B': [('A', 4), ('C', 8), ('H', 11)],
    'C': [('B', 8), ('D', 7), ('F', 4), ('I', 2)],
    'D': [('C', 7), ('E', 9), ('F', 14)],
    'E': [('D', 9), ('F', 10)],
    'F': [('C', 4), ('D', 14), ('E', 10), ('G', 2)],
    'G': [('F', 2), ('H', 1), ('I', 6)],
    'H': [('A', 8), ('B', 11), ('I', 7), ('G', 1)],
    'I': [('C', 2), ('G', 6), ('H', 7)]
}

data_set_2 = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 3), ('D', 2), ('E', 3)],
    'C': [('B', 1), ('D', 4), ('E', 5)],
    'D': [],
    'E': [('D', -5)]
}

sample_graph = a_graph
num_of_vertex = len(sample_graph)
weight = {}
for a_key in sample_graph.iterkeys():
    weight[a_key] = sys.maxint

weight['A'] = 0
in_order = sorted(sample_graph)
for key in in_order:
    neighbours = sample_graph[key]
    for node in neighbours:
        cost = weight[key] + node[1]
        current_cost = weight[node[0]]
        if cost < current_cost:
            weight[node[0]] = cost

print(weight)

