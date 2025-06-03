class binaryHeap:

  def __init__(self, heap):
    self.heap = heap

  def parent(self, i):
    return i//2
  
  def left(self, i):
    return 2*i+1
  
  def right(self, i):
    return 2*i+2

  '''
  Опускаем узел, который не удволетворяет условия
  невозрастающего дерева, рекурсивно
  '''  
  def maxHeapify(self, i):
    l = self.left(i)
    r = self.right(i)
    heap = self.heap
    if l < len(heap) and heap[l] > heap[i]:
      largest = l
    else:
      largest = i

    if r < len(heap) and heap[r] > heap[largest]:
      largest = r

    if largest != i:
      num = heap[i]
      heap[i] = heap[largest]
      heap[largest] = num
      self.maxHeapify(largest)


  '''
  Строим пирамиду с листьев
  '''
  def buildMaxHeap(self):
    heap = self.heap
    for i in range(len(heap)//2-1, -1, -1):
      self.maxHeapify(i)

'''
Опускаем элемент, который не удволетворяет условиям невозрастающего дерева
'''
def maxHeapifyWithCycle(heap, i):
  while i < len(heap)//2:
    left = i*2+1
    right = i*2+2

    if heap[right] > heap[left]:
      num = heap[left]
      heap[left] = heap[right]
      heap[right] = num

    if heap[left] > heap[i]:
      num = heap[left]
      heap[left] = heap[i]
      heap[i] = num
      i = left
    elif heap[right] > heap[i]:
      num = heap[right]
      heap[right] = heap[i]
      heap[i] = num
      i = right
    

heap1 = [27,17,3,16,13,10,1,5,7,12,4,8,9,0]
heap2 = [4,1,3,2,16,9,10,14,8,7]

maxHeapifyWithCycle(heap1, 2)
print(heap1)

tree = binaryHeap(heap1)
tree.buildMaxHeap()
print(tree.heap)



'''
Пирамида - почти полное бинарное дерево(не всегда заполнен последний  уровень)
Поиск за log n

Существуют неубывающие и невозрастающие пирамиды
Неубыващие:
Родитель <= потомок
В корне - минимум

Невозрастающее:
Родитель >= потомок
В корне - максимум

Сортировка за n*log n
Остальные процедуры за log n

'''