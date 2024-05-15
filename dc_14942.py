def reverse_graph(graph):
    reversed_graph = {}
    for node in graph:
        reversed_graph[node] = []
    
    for node in graph:
        for neighbor in graph[node]:
            reversed_graph[neighbor].append(node)
    
    return reversed_graph

graph = {
    'a': ['b', 'c'],
    'b': ['c'],
    'c': ['d'],
    'd': []
}

print(reverse_graph(graph)) # {'a': [], 'b': ['a'], 'c': ['a', 'b'], 'd': ['c']}