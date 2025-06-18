import random

class Environment:
    def __init__(self):
        self.state = { 'A': random.randint(0, 1),
                       'B': random.randint(0, 1),
                       'C': random.randint(0, 1),
                       'D': random.randint(0, 1) }
        
class utilityreflex:
    def __init__(self, environment):
        self.environment = environment
        self.performance = 0
        self.location = 'A'

    def next_dirty_location(self, states, current_location):
        for location in states:
            if states[location] == 1 and location != current_location:
                return location
        return None

    def act(self):
        while 1 in self.environment.state.values():
            print(f"Current location: {self.location}")
            if self.environment.state[self.location] == 1:  # dirty
                print(f"Cleaning {self.location}")
                self.environment.state[self.location] = 0  # Clean 
                self.performance += 10 #cost for cleaning
            else:
                print(f"{self.location} is already clean")
                next_location = self.next_dirty_location(self.environment.state, self.location)
                if next_location:
                    print(f"Moving to {next_location}")
                    self.location = next_location
                    self.performance -= 1  # Small cost for moving
                else:
                    print("No dirty locations left.")
                    break
            print(f"Performance: {self.performance}\n")


env = Environment()
agent = utilityreflex(env)
agent.act()