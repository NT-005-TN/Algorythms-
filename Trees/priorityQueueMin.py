from binaryHeap import binaryHeap
class priorityQueue(binaryHeap):

  def __init__(self, heap):
    self.heap = heap
    self.buildMinHeap()

  def buildMinHeap(self):
    heap = self.heap
    for i in range(len(heap)//2-1, -1, -1):
      self.minHeapify(len(heap), i)

  def minHeapify(self, lenght, i):
    l = self.left(i)
    r = self.right(i)
    heap = self.heap

    if (l < lenght) and (heap[l] < heap[i]):
      smallest  = l
    else:
      smallest = i

    if (r < lenght) and (heap[r] < heap[smallest]):
      smallest = r
    
    if smallest != i:
      num = heap[i]
      heap[i] = heap[smallest]
      heap[smallest] = num
      self.minHeapify(lenght, smallest)

  # O(1)
  def heapMinimum(self):
    return self.heap[0]
  
  # O(log n)
  def heapExtractMin(self):
    heap = self.heap 
    lenght = len(heap)
    if lenght == 0:
      return "Error: empty queue"
    
    mx = heap[0]
    heap[0] = heap[lenght-1]
    lenght -= 1
    self.minHeapify(lenght, 0) 
    return mx
  
  # O(log n) 
  def heapDecreaseKey(self, i, key):
    heap = self.heap
    if (key > heap[i]):
      return "Error: new key is bigger than present key"
    
    heap[i] = key
    parent = self.parent(i)
    while (i > 0) and (heap[parent] > heap[i]):
      num = heap[i]
      heap[i] = heap[parent]
      heap[parent] = num
      i = parent
  
  # O(log n)
  def minHeapInsert(self, key):
    self.heap.append(float("+Inf"))
    self.heapDecreaseKey(len(self.heap)-1, key)

  def heapDelete(self, i):
    heap = self.heap
    l = self.left(i)
    r = self.right(i)

      

heap = [15,13,9,5,12,8,7,4,0,6,2,1]
queue1 = priorityQueue(heap)
print(queue1.heap)
print(queue1.heapMinimum())
print(queue1.heapExtractMin())
queue1.heapDecreaseKey(4, 0)
print(queue1.heap)
queue1.minHeapInsert(0)
print(queue1.heap)