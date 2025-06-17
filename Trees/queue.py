
class queue:

  def __init__(self, n):
    self.heap = [0 for _ in range(n)]
    self.tail = 0
    self.head = 0
    self.size = 0
    self.capacity = n

  def enqueue_end(self, x):
    if self.size == self.capacity:
      raise Exception("Queue is full")
    self.heap[self.tail] = x
    self.tail = (self.tail + 1) % self.capacity
    self.size += 1

  def dequeue_start(self):
    if self.size == 0:
      raise Exception("Queue is empty")
    x = self.heap[self.head]
    self.head = (self.head + 1) % self.capacity
    self.size -= 1
    return x
  
  def enqueue_start(self, x):
    if self.size == self.capacity:
      raise Exception("Queue is full")
    self.head = (self.head - 1) % self.capacity
    self.heap[self.head] = x
    self.size += 1

  def dequeue_end(self):
    if self.size == 0:
      raise Exception("Queue is empty")
    self.tail = (self.tail - 1) % self.capacity
    x = self.heap[self.tail]
    self.size -= 1
    return x
  
queue1 = queue(10)
info = [2,4,6,8,10,12,14,16,18,20]
for x in info:
  queue1.enqueue_start(x)
  print(queue1.heap)
  print(queue1.head, queue1.tail)

for i in range(3):
  queue1.dequeue_end()
  print(queue1.heap)
  print(queue1.head, queue1.tail)
  
dq = queue(10)

for x in [10, 20, 30]:
    dq.enqueue_start(x)
print("After enqueue_start:", dq.heap)

dq.enqueue_end(5)
print("After enqueue_end(5):", dq.heap)

print("dequeue_start", dq.dequeue_start())
print("After dequeue_start:", dq.heap, dq.size)

print("dequeue_end:", dq.dequeue_end())
print("After dequeue_end:", dq.heap, dq.size)