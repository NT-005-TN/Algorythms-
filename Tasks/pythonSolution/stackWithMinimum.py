
#https://leetcode.com/problems/min-stack/

class MinStack:

  def __init__(self):
    self.stack = []
    self.minStack = []
  
  def push(self, x):
    self.stack.append(x)
    self.minStack.append(x)
