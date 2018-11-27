import sys
a_graph = {
    'A': [('B', -1), ('C', 4)],
    'B': [('D', 1), ('C', 3), ('E', 2)],
    'C': [],
    'D': [('B', 2), ('C', 5)],
    'E': [('D', -3)],
}


num_of_vertex = len(a_graph)
weight = {}
for a_key in a_graph.iterkeys():
    weight[a_key] = sys.maxint

weight['A'] = 0
for key in a_graph.iterkeys():
    neighbours = a_graph[key]
    for node in neighbours:
        cost = weight[key] + node[1]
        current_cost = weight[node[0]]
        if cost < current_cost:
            weight[node[0]] = cost

print(weight)
