class qItem:
  def __init__(self, val, next=None, pre=None):
    self.val = val
    self.next = next if type(next) is qItem else None
    self.pre = pre if type(pre) is qItem else None


class Queue:
  def __init__(self, first=None):
    self.tail = self.head = first if type(first) is qItem else None
    self.size = 0 if self.tail is None else 1

  def len(self):
    return self.size

  def isEmpty(self):
    return bool(self.len() == 0)

  def peek(self):
    return False if self.isEmpty() else self.head.val

  def enqueue(self, val):
    self.size += 1
    if self.isEmpty():
      self.head = self.tail = qItem(val)
    else:
      oldTail = self.tail
      tail = self.tail = qItem(val, oldTail)
      oldTail.pre = tail
    return self.tail

  def dequeue(self):
    if self.isEmpty():
      return False
    else:
      self.size -= 1
      poped = self.head
      self.head = self.head.pre
      self.head.next = None
      poped.next, poped.pre = None, None
      return poped.val
