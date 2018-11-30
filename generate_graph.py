import Dijkstras as perform
import sys
import networkx as nx
import random
import time

# To generate N vertices set the size below
n_vertices = 1000
G=nx.complete_graph(n_vertices)

g_with_weigths = nx.Graph()

list_with_weight = []
for edge in G.edges():
    weight = random.randint(1, 20)
    list_with_weight.append((edge[0], edge[1], weight))

# print(list_with_weight)
graph_with_weight = {}
for elem in list_with_weight:
    node = elem[0]
    if node in graph_with_weight:
        neighbours = graph_with_weight[node]
        neighbours.append((elem[1], elem[2]))
    else:
        graph_with_weight[node] = [(elem[1], elem[2])]

# print(graph_with_weight)

# start = time.time()
# perform.dijkstras(graph_with_weight, 0)
# end = time.time()
# print(end - start)

# Bellman Ford implementation
def bellman(a_graph, initial_node):
    weight = {}
    for a_key in a_graph.iterkeys():            # initialize every vertex to infinity
        weight[a_key] = sys.maxint

    weight[initial_node] = 0                    # set the cost of the initial node
    for key in a_graph.iterkeys():              # start exploring all the vertices
        neighbours = a_graph[key]               # get neighbours from vertex key
        for node in neighbours:                 # for each neighbour
            cost = weight[key] + node[1]        # calculate temp cost
            if node[0] in weight:               # check for seg-fault
                current_cost = weight[node[0]]
                if cost < current_cost:         # if the new cost is smaller
                    weight[node[0]] = cost      # update cost

#     print(weight)
#
# print("My implementation")
# start = time.time()
# bellman(graph_with_weight, 0)
# end = time.time()
# print(end - start)

start = time.time()
G.add_weighted_edges_from(list_with_weight)
# print(G.adj)
length = nx.single_source_bellman_ford(G,0)
end = time.time()
print(end - start)