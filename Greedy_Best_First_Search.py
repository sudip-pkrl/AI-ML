import heapq

def greedy_best_first_search(graph, heuristics, start, goal):
    frontier = [(heuristics[start], [start])]
    visited = set()

    while frontier:
        _, path = heapq.heappop(frontier)
        current = path[-1]

        if current == goal:
            return path

        if current in visited:
            continue
        visited.add(current)

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(frontier, (heuristics[neighbor], path + [neighbor]))

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

heuristics = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 6,
    'G': 0
}

start_node = 'A'
goal_node = 'G'
path = greedy_best_first_search(graph, heuristics, start_node, goal_node)

print("Path:", path)