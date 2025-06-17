
class stackTail:

  def __init__(self, n):
    self.tail = 0
    self.heap = [0] * n
    self.size = 0
    self.capacity = n

  
  def enqueue(self, x):
    if self.size == self.capacity:
      raise Exception("Queue is full")
    self.heap[self.tail] = x
    self.tail = (self.tail + 1) % self.capacity
    self.size += 1

class stackHead:
  def __init__(self, tail_ref):
    self.head = 0
    self.tail_ref = tail_ref

  def dequeue(self):
    if self.tail_ref.size == 0:
      raise Exception("Queue is empty")
    x = self.tail_ref.heap[self.head]
    self.head = (self.head + 1) % self.tail_ref.capacity
    self.tail_ref.size -= 1
    return x
  
class newQueue(stackHead, stackTail):

  def __init__(self, n):
    self.tail_part = stackTail(n)
    self.head_part = stackHead(self.tail_part)

  def enqueue(self, x):
    self.tail_part.enqueue(x)

  def dequeue(self):
    return self.head_part.dequeue()

  @property
  def heap(self):
    return self.tail_part.heap

  @property
  def size(self):
    return self.tail_part.size

  @property
  def capacity(self):
    return self.tail_part.capacity
  

qu = newQueue(10)

info = [0,2,4,6,8,10,12,14,16,18]
for x in info:
  qu.enqueue(x)
  print(qu.heap)
  print(qu.size)
  print()

for i in range(3):
  print(qu.dequeue())
  print(qu.size)
  print()
