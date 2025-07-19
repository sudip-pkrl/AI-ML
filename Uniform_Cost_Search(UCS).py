import heapq

def uniform_cost_search(graph, start, goal):
    frontier = [(0, [start])]
    visited = set()

    while frontier:
        cost, path = heapq.heappop(frontier)
        current = path[-1]

        if current == goal:
            return path, cost

        if current in visited:
            continue
        visited.add(current)

        for neighbor, edge_cost in graph.get(current, []):
            if neighbor not in visited:
                total_cost = cost + edge_cost
                heapq.heappush(frontier, (total_cost, path + [neighbor]))

    return None, float('inf')

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

start_node = 'A'
goal_node = 'D'
path, cost = uniform_cost_search(graph, start_node, goal_node)

print("Path:", path)
print("Total cost:", cost)