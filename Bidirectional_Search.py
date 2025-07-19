from collections import deque

def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    front_visited = {start: [start]}
    back_visited = {goal: [goal]}

    front_queue = deque([start])
    back_queue = deque([goal])

    while front_queue and back_queue:
        if front_queue:
            current_front = front_queue.popleft()
            for neighbor in graph.get(current_front, []):
                if neighbor not in front_visited:
                    front_visited[neighbor] = front_visited[current_front] + [neighbor]
                    front_queue.append(neighbor)
                    if neighbor in back_visited:
                        return front_visited[neighbor] + back_visited[neighbor][-2::-1]

        if back_queue:
            current_back = back_queue.popleft()
            for neighbor in graph.get(current_back, []):
                if neighbor not in back_visited:
                    back_visited[neighbor] = back_visited[current_back] + [neighbor]
                    back_queue.append(neighbor)
                    if neighbor in front_visited:
                        return front_visited[neighbor] + back_visited[neighbor][-2::-1]

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
path = bidirectional_search(graph, start_node, goal_node)

print("Path:", path)