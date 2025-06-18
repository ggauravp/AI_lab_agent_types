import random

class Environment:
    def __init__(self):
        self.state = { 'A': random.randint(0,1),
                       'B': random.randint(0,1),
                       'C': random.randint(0,1),
                       'D': random.randint(0,1) }
    

class SimpleReflexAgent:
    def __init__(self, environment):
        self.environment = environment
        self.positions = list(environment.state.keys())  # ['A', 'B', 'C', 'D']
        self.current_position = random.choice(self.positions)  # Start at random position

    def run(self):
        max_steps = 10  # Limit steps to avoid infinite loop
        for _ in range(max_steps):
            # Check current position's state
            if self.environment.state[self.current_position] == 1:  # Dirty
                print(f"Cleaning {self.current_position}")
                self.environment.state[self.current_position] = 0  # Clean it
            else:  # Clean
                print(f"{self.current_position} is already clean")
            # Move to a random position
            self.current_position = random.choice(self.positions)
        
        # Print final state to see results
        for pos in self.environment.state:
            status = "clean" if self.environment.state[pos] == 0 else "dirty"
            print(f"{pos} is {status}")

# Create environment and agent
env = Environment()
agent = SimpleReflexAgent(env)
print("Initial Environment State:", env.state)
agent.run()