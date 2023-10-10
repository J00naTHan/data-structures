class linkedList:
  def __init__(self):
    self.size = 0
    self.head = None

  def findTail(self):
    current = self.head
    while current.next is not None:
      current = current.next
    return current
  
  def insert(self, val):
    self.size += 1
    node = Node(val)
    if self.head is None:
      self.head = node
      return self.head
    tail, tail.next = self.findTail(), node
    return tail

  def delete(self, val):
    current = self.head
    self.size -= 1
    while current.val != val:
      previous, current = current, current.next
    previous.next, current.val, current.next = current.next, None, None
    return current

  def list(self):
    limit, current, str = self.findTail(), self.head, ''
    while limit != current:
      str += f"{current.val} -> "
      current = current.next
    str += f"{current.val}"
    print(f"{str}\n\nTamanho da Lista: {self.size}")

class Node:
  def __init__(self, valor, next = None):
    self.val = valor
    self.next = next

if __name__ == "__main__":
  list = linkedList()
  list.insert(16)
  list.insert(5)
  list.insert(20)
  list.insert(1)
  list.delete(20)
  list.findTail()
  list.list()
