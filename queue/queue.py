class qItem:
#método construtor de cada item da fila
  def __init__(self, val, next=None, pre=None):
    self.val = val
    self.next = next if type(next) is qItem else None
    self.pre = pre if type(pre) is qItem else None

#método built-in str para definir uma forma em string para o valor de cada item da fila
  def __str__(self):
    return self.val


class Queue:
#método construtor da estrutura de fila
  def __init__(self, first=None):
    self.tail = self.head = first if type(first) is qItem else None
    self.size = 0 if self.tail is None else 1

#método built-in iter e next para iterar pelos itens da fila
  def __iter__(self):
    self.count = 0
    self.current = self.tail
    return self

  def __next__(self):
    if self.count < len(self):
      self.current = self.current.next if self.count != 0 else self.current
      self.count += 1
      return self.current.val
    else:
      raise StopIteration

#método built-in len para permitir cálculo do comprimento da fila
  def __len__(self):
    return self.size

#método para verificar se a fila está vazia
  def isEmpty(self):
    return bool(self.__len__() == 0)

#método que retorna, sem modificar, o elemento do topo da fila
  def peek(self):
    return False if self.isEmpty() else self.head.val

#método para inserir um item na cauda (final) da fila
  def enqueue(self, val):
    self.size += 1
    if self.isEmpty():
      self.head = self.tail = qItem(val)
    else:
      oldTail = self.tail
      tail = self.tail = qItem(val, oldTail)
      oldTail.pre = tail
    return self.tail

#método para retirar um item da cabeça (topo) da fila
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
