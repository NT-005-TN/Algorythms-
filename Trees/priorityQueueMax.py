from binaryHeap import binaryHeap
class priorityQueue(binaryHeap):

  def __init__(self, heap):
    super().__init__(heap)
    super().buildMaxHeap()

  # O(1)
  def heapMaximum(self):
    return self.heap[0]
  
  # O(log n)
  def heapExtractMax(self):
    heap = self.heap 
    lenght = len(heap)
    if lenght == 0:
      return "Error: empty queue"
    
    mx = heap[0]
    heap[0] = heap[lenght-1]
    lenght -= 1
    super().maxHeapify(lenght-1, 0) 
    return mx
  
  # O(log n) 
  def heapIncreaseKey(self, i, key):
    heap = self.heap
    if (key < heap[i]):
      return "Error: new key is smaller than present key"
    
    heap[i] = key
    parent = self.parent(i)
    while (i > 0) and (heap[parent] < heap[i]):
      num = heap[i]
      heap[i] = heap[parent]
      heap[parent] = num
      i = parent
  
  # O(log n)
  def maxHeapInsert(self, key):
    heap = self.heap
    heap.append(float("-Inf"))
    self.heapIncreaseKey(len(heap)-1, key)

  
heap1 = [27,17,3,16,13,10,1,5,7,12,4,8,9,0]
queue1 = priorityQueue(heap1)
for i in range(1):
  print(queue1.heapExtractMax())

print(queue1.heap)
queue1.heapIncreaseKey(5, 26)
print(queue1.heap)

queue1.maxHeapInsert(20)
print(queue1.heap)
  
heap2 = [15,13,9,5,12,8,7,4,0,6,2,1]
queue2 = priorityQueue(heap2)
print(queue2.heapExtractMax())
queue2.maxHeapInsert(10)
print(queue2.heap)
