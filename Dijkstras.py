import sys
import heapq

graph = {
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

# initializing the distance
init_list = {}
for key in graph:
    temp = (key, sys.maxint, None)
    init_list[key] = temp

initial_vertex = init_list['A']
print(initial_vertex)

# temp = list(initial_vertex)
# temp[1] = 0
# temp = tuple(temp)
# init_list['A'] = temp
#
# current_list = []
# for value in init_list.itervalues():
#     temp = (value[1], value[0], value[2])
#     current_list.insert(0, temp)
#
# heapq.heapify(current_list)
# print(current_list)
# visited = {'A' : 0}
# while current_list:
#     temp = heapq.heappop(current_list)
#     neighbours = graph[temp[1]]
