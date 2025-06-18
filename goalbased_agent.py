import random
class Environment:
    def __init__(self):
        self.state = { 'A': random.randint(0,1),
                       'B': random.randint(0,1),
                       'C': random.randint(0,1),
                       'D': random.randint(0,1) }
        
    def is_goal_state(self):
        for status in self.state.values():
            if status != 0:  # If we find any dirty position
                return False  # Goal not reached yet
        return True  # All positions are clean

class GoalBasedAgent:
    def __init__(self, environment):
        self.environment = environment
        self.positions = list(environment.state.keys())
        # self.positions = ['A', 'B', 'C', 'D']  
        self.current_index = 0

    def run(self):
        if self.environment.is_goal_state():
            print("already in goal state")
            return
        
        while self.current_index < len(self.positions):
            current_position = self.positions[self.current_index]
            if self.environment.state[current_position] == 1:
                print(f"cleaning {current_position}")
                self.environment.state[current_position] = 0
            else:
                print(f"{current_position} is already cleaned")

            self.current_index+= 1

        for i in self.environment.state:
            if self.environment.state[i] == 1:
                print(f"{i} is still dirty")
            else:
                print(f"{i} is clean now")

       
env = Environment()
agent = GoalBasedAgent(env)
print("Initial Environment State:", env.state)
agent.run()