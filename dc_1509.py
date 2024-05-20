def is_minimally_connected(graph):
    def dfs(node, parent, visited):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if not dfs(neighbor, node, visited):
                    return False
            elif neighbor != parent:
                return False
        return True
    visited = set()
    start_node = next(iter(graph))
    
    if not dfs(start_node, None, visited):
        return False
    
    if len(visited) != len(graph):
        return False

    num_vertices =  len(graph)
    num_edges = sum(len(neighbors) for neighbors in graph.values()) // 2

    return num_edges == num_vertices - 1  

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

print(is_minimally_connected(graph))  # True