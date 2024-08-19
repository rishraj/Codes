#
# @lc app=leetcode id=622 lang=python3
#
# [622] Design Circular Queue
#

# @lc code=start

# linked list implementation of circular queue
""" class Node:
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
        return self.cur_size == self.size """


class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None]*k # initialising the queue
        self.size = k
        self.cur_size = 0
        self.first = 0
        self.last = -1 # start at -1 so that 1st enQueue happens at 0 (imp)

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.last = (self.last + 1) % self.size
        self.q[self.last] = value
        self.cur_size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.first = (self.first + 1) % self.size # no need to remove earlier self.first (it's just garbage)
        self.cur_size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.q[self.first]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.q[self.last]

    def isEmpty(self) -> bool:
        return self.cur_size == 0

    def isFull(self) -> bool:
        return self.cur_size == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end

