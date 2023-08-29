class IO:
  def __init__(self, action):
    self.action = action

  def run(self):
    return self.action()

def io_reduce(actions):
  results = []
  for action in actions:
    result = action.run()
    results.append(result)
  return results

def input_action():
  return input("Enter something: ")

def print_action():
  print("Hello, World!")
  return "Hello"

actions = [IO(input_action), IO(print_action)]
results = io_reduce(actions)
print(results)