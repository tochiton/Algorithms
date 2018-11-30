from sys import maxint as maxint
import heapq


graph_data = {
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


class Node:
    def __init__(self, name, weight=maxint, parent=None):
        self.name = name
        self.weight = weight
        self.parent = parent
        self.neighbours = []

    @property
    def name(self):
        return self.name

    @property
    def weight(self):
        return self.weight

    def set_weight(self, val):
        self.weight = val

    def add_edge(self, node):
        self.neighbours.append(node)

    def get_neighbours(self):
        return self.neighbours

    def display_children(self):
        print("Parent {}".format(self.name))
        for child in self.neighbours:
            print("Child {} {}".format(child.name, child.weight))


class graph:
    def __init__(self):
        self.adj_list = {}

    def get_graph_length(self):
        return len(self.adj_list)

    def add_vertex(self, name, a_node):
        self.adj_list[name] = a_node

    def delete_node(self, name):
        if self.adj_list[name]:
            del self.adj_list[name]
            return True
        else:
            print("can't delete node, no name {}".format(name))

    def get_node(self, name):
        if name in self.adj_list:
            return self.adj_list[name]
        return None

    def update_weight(self, node_name, val):
        if self.adj_list[node_name]:
            temp_node = self.adj_list[node_name]
            temp_node.set_weight(val)
            return
        else:
            print("no node key in dict {}".format(node_name))

    def display_graph(self):
        for key, a_node in self.adj_list.iteritems():
            a_node.display_children()
            print("******************")

    def get_lowest_node(self):
        temp_max = maxint
        node_lowest_cost = ''
        for child in self.adj_list.itervalues():
            if child.weight < temp_max:
                node_lowest_cost = child.name
                temp_max = child.weight
        return self.adj_list[node_lowest_cost]


def loader(a_graph):
    root = graph()
    for key, value in a_graph.iteritems():
        parent_node = Node(key)
        for neighbour in value:
            child = Node(neighbour[0], neighbour[1], key)
            parent_node.add_edge(child)
        root.add_vertex(key, parent_node)
    return root


def dijkstras(a_graph, initial_node):
    root = loader(a_graph)                          # instantiate a graph
    # initial node
    root.update_weight(initial_node, 0)             # set the weight of the initial node to 0
    path = []
    visited = set()                                 # keeps track of the visited vertices
    while root.get_graph_length() > 0:              # repeats the algorithm until of vertices have been visited
        parent_node = root.get_lowest_node()        # pop the vertices with the lowest cost
        for a_neighbour in parent_node.get_neighbours():            # explore all its neighbours
            if a_neighbour.name not in visited:
                cost = parent_node.weight + a_neighbour.weight      # calculate temp cost
                a_neighbour_in_the_hood = root.get_node(a_neighbour.name)
                if a_neighbour_in_the_hood:                         # double check there is a cost associated
                    current_cost = a_neighbour_in_the_hood.weight   # fetch cost
                    if cost < current_cost:                         # compare if the new cost is smaller
                        root.update_weight(a_neighbour.name, cost)  # if so, update it
        path.append((parent_node.name, parent_node.weight))         # append the popped node to the path
        visited.add(parent_node.name)                               # mark it as visited
        name_deleted_node = parent_node.name
        root.delete_node(name_deleted_node)                         # removes the node from the exploring list


    print(path)



dijkstras(graph_data, 'A')












