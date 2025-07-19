def simple_reflex_agent(percept):
    rules = {
        "dirty": "clean",
        "clean": "move"
    }
    action = rules.get(percept, "move")
    return action

percepts = ["dirty", "clean", "dirty", "clean"]
for p in percepts:
    print(f"Percept: {p} → Action: {simple_reflex_agent(p)}")