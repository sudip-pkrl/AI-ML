def dls(graph, node, goal, limit, path):
    if node == goal:
        return path
    if limit <= 0:
        return None
    for neighbor in graph.get(node, []):
        if neighbor not in path:
            result = dls(graph, neighbor, goal, limit - 1, path + [neighbor])
            if result:
                return result
    return None

def idfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        result = dls(graph, start, goal, depth, [start])
        if result:
            return result
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

start_node = 'A'
goal_node = 'G'
max_depth = 5
path = idfs(graph, start_node, goal_node, max_depth)

print("Path:", path)