class binaryHeap:
  
  def __init__(self, heap):
    self.heap = heap

  def parent(self, i):
    return i//2
  
  def left(self, i):
    return 2*i+1
  
  def right(self, i):
    return 2*i+2
  
# Опускаем узел, который не соответсвтвует условиям невозрастающего дерева
  # O(log n)
  def maxHeapify(self, lenght, i):
    l = self.left(i)
    r = self.right(i)
    heap = self.heap

    if (l < lenght) and (heap[l] > heap[i]):
      largest = l
    else:
      largest = i

    if (r < lenght) and (heap[r] > heap[largest]):
      largest = r
    
    if largest != i:
      num = heap[i]
      heap[i] = heap[largest]
      heap[largest] = num
      self.maxHeapify(lenght, largest)
  
  # O(n*log n)
  def buildMaxHeap(self):
    lenght = len(self.heap)
    for i in range((lenght)//2-1, -1, -1):
      self.maxHeapify(lenght, i)

  # O(n*log n)
  def buildMaxHeapWithCycle(self):
    for i in range(len(self.heap)//2-1, -1, -1):
      self.maxHeapifyWithCycle(i)
  
  # O(log n)
  def maxHeapifyWithCycle(self, i):
    heap = self.heap
    while i < len(heap):
      l = self.left(i)
      r = self.right(i)

      if (l < len(heap)) and (heap[l] > heap[i]):
        largest = l
      else:
        largest = i

      if (r < len(heap)) and (heap[r] > heap[largest]):
        largest = r
      
      if largest != i:
        num = heap[i]
        heap[i] = heap[largest]
        heap[largest] = num
        i = largest
      else:
        break
  
  # O(n*log n)
  def heapSort(self):
    self.buildMaxHeap()
    heap = self.heap
    for i in range(len(heap)-1, 0, -1):
      num = heap[i]
      heap[i] = heap[0]
      heap[0] = num
      self.maxHeapify(i, 0)

heap1 = [27,17,3,16,13,10,1,5,7,12,4,8,9,0]
binHeap1 = binaryHeap(heap1)
binHeap1.buildMaxHeap()
print(binHeap1.heap)

binHeap2 = binaryHeap(heap1)
binHeap2.buildMaxHeapWithCycle()
print(binHeap2.heap)

binHeap3 = binaryHeap(heap1)
binHeap3.heapSort()
print(binHeap3.heap)


''' Пусть это будет невозрастающее дерево '''
''' Т.е parent >= child'''

'''

Логика maxHeapify
У нас есть узел i(i - его номер в списке).
Дерево невозрастающее или, очень грубо говоря(для понимания), убывающее
Т.е дети <= родителя
Значит, берем наш узел и сравниваем его с детьми.
Берем левого ребенка и правого ребенка(left и right)
Сначала, допустим, берем левого. 
Если он больше родителя, то пусть его индекс - наибольший
Правого проверяем уже с наибольшим элементом 
Если все меньше родителя, то наибольший индекс - родительский.
В конце алгоритма, если наибольший индекс не родительский,
то меняем элемент наибольшего индекса с родительским.

'''



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