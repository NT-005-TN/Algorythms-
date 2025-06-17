
class QueueWithTwoStacks:

  def __init__(self):
    self.stack1 = []
    self.stack2 = []

  def enqueue(self, x):
    self.stack1.append(x)
  
  def dequeue(self):
    if not self.stack2:
      if not self.stack1:
        raise Exception("Queue is empty")

      while self.stack1:
        self.stack2.append(self.stack1.pop())
    
    return self.stack2.pop()
    

qu = QueueWithTwoStacks()

info = [0,2,4,6,8,10,12,14,16,18]
for x in info:
  qu.enqueue(x)
  print(qu.stack1, qu.stack2)
  print()

for i in range(3):
  print(qu.dequeue())
  print(qu.stack1, qu.stack2)
  print()
