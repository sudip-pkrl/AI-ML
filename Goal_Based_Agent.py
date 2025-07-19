def goal_based_agent(percept, goal):
    if percept == goal:
        return "stop"
    elif percept == "dirty":
        return "clean"
    else:
        return "move to next"

percepts = ["dirty", "clean", "goal"]
goal = "goal"
for p in percepts:
    print(f"Percept: {p} → Action: {goal_based_agent(p, goal)}")