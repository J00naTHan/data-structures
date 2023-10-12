class Item:
  def __init__(self, val, pre = None):
    self.val = val
    self.pre = pre if pre is None or type(pre) is Item else None

class Stack:
  def __init__(self, top = None):
    self.top = top if top is None or type(top) is Item else None
    self.size = 0 if top is None else 1

  def len(self):
    return self.size

  def peek(self):
    return False if self.top is None else self.top.val
  
  def isEmpty(self):
    return bool(self.len() == 0)
  
  def push(self, val):
    self.size += 1
    if self.isEmpty():
      self.top = Item(val)
    else:
      pre = self.top
      self.top = Item(val, pre)
    return self.top

  def pop(self):
    if self.isEmpty():
      return False
    else:
      self.size -= 1
      poped = self.top
      self.top = self.top.pre
      return poped.val
