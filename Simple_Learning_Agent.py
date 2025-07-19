class LearningAgent:
    def __init__(self):
        self.memory = {}

    def perceive_and_act(self, percept):
        if percept in self.memory:
            return self.memory[percept]
        else:
            action = "clean" if percept == "dirty" else "move"
            self.memory[percept] = action
            return action

agent = LearningAgent()
percepts = ["dirty", "clean", "dirty", "clean", "goal"]
for p in percepts:
    print(f"Percept: {p} → Action: {agent.perceive_and_act(p)}")

print("\nLearned memory:", agent.memory)