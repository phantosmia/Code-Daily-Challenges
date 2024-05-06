def reverse_graph(graph):

    reversed_graph = {vertex: [] for vertex in graph}

    for vertex, edges in graph.items():
        for edge in edges:
            reversed_graph[edge].append(vertex)
    return reversed_graph

graph = {
    'a': ['b', 'c'],
    'b': ['c'],
    'c': ['d'],
    'd': []
}

print(reverse_graph(graph)) # {'a': [], 'b': ['a'], 'c': ['a', 'b'], 'd': ['c']}