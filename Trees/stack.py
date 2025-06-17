
class stack:

  def __init__(self):
    self.stack = []
    self.top = -1
  
  def stackEmpty(self):
    if self.top == 0:
      return True
    return False
  
  def push(self, x):
    self.top += 1
    self.stack.append(x)

  def pop(self):
    if self.stackEmpty():
      return "Underflow"
    last = self.stack.pop()
    self.top -= 1
    return last
  

stack = stack()
info = [0,2,4,6,8,10,12]
for x in info:
  stack.push(x)
  print("top = ", stack.top)
  print()

print("poped", stack.pop())
print("top = ", stack.top)
  