import heapq

def a_star_search(graph, heuristics, start, goal):
    frontier = [(heuristics[start], 0, [start])]
    visited = {}

    while frontier:
        est_total_cost, cost_so_far, path = heapq.heappop(frontier)
        current = path[-1]

        if current == goal:
            return path, cost_so_far

        if current in visited and visited[current] <= cost_so_far:
            continue
        visited[current] = cost_so_far

        for neighbor, edge_cost in graph.get(current, []):
            new_cost = cost_so_far + edge_cost
            if neighbor not in visited or visited[neighbor] > new_cost:
                est_cost = new_cost + heuristics.get(neighbor, float('inf'))
                heapq.heappush(frontier, (est_cost, new_cost, path + [neighbor]))

    return None, float('inf')

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

heuristics = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 0
}

start_node = 'A'
goal_node = 'D'
path, cost = a_star_search(graph, heuristics, start_node, goal_node)

print("Path:", path)
print("Total cost:", cost)