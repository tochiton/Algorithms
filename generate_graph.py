import networkx as nx
import random

G=nx.complete_graph(5)

g_with_weigths = nx.Graph()

# all_edges = G.edges()
# for edge in all_edges:
#     cost = random.randint(1, 20)
#     g_with_weigths.add_node(edge[0], edge[1], weight = 1.2)
#     # print(edge[0], edge[1])

for edge in G.edges():
    print(edge)

# DG=nx.DiGraph()
# DG.add_weighted_edges_from([(1,2,0.5), (3,1,0.75)])
# DG.out_degree(1,weight='weight')