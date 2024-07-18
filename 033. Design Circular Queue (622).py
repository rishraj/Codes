# doubly linked list implementation of circular queue
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyCircularQueue:
    def __init__(self, k: int):
        self.size = k
        self.cur_size = 0
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
            self.cur_size += 1
            return True
        self.tail.next = Node(value)
        self.tail = self.tail.next
        self.cur_size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        if self.cur_size == 1:
            self.head = None
            self.tail = None
            self.cur_size -= 1
            return True
        self.head = self.head.next
        self.cur_size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.head.val

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.head == None

    def isFull(self) -> bool:
        return self.cur_size == self.size
