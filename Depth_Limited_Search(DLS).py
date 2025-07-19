def depth_limited_search(graph, start, goal, limit):
    def recursive_dls(node, path, depth):
        if node == goal:
            return path
        if depth == 0:
            return None
        for neighbor in graph.get(node, []):
            if neighbor not in path:
                result = recursive_dls(neighbor, path + [neighbor], depth - 1)
                if result:
                    return result
        return None

    return recursive_dls(start, [start], limit)

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
depth_limit = 3
path = depth_limited_search(graph, start_node, goal_node, depth_limit)

print("Path:", path)