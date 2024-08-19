#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#

# @lc code=start

class Node:
    def __init__(self, val):
        # double linked list
        """  self.val = val
        self.prev = None
        self.next = None """
        
        self.val = val
        self.next = None
        
class MyLinkedList:

    def __init__(self):
         # double linked list
        """ self.left = Node(-1)
        self.right = Node(-1)
        self.left.next = self.right
        self.right.prev = self.left """
        
        self.head = Node(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        # double linked list
        """ cur, i = self.left.next, 0
        while cur and i < index:
            cur = cur.next
            i += 1
        if cur and cur != self.right:
            return cur.val
        return -1 """
        
        cur, i = self.head.next, 0
        while cur and i < index:
            cur = cur.next
            i += 1
        if cur:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        # double linked list
        """ tmp = self.left.next
        self.left.next = Node(val)
        self.left.next.prev = self.left
        self.left.next.next = tmp
        tmp.prev = self.left.next """
        
        tmp = self.head.next
        self.head.next = Node(val)
        self.head.next.next = tmp
        if not self.head.next.next:  # update tail for 1st added element at head
            self.tail = self.head.next

    def addAtTail(self, val: int) -> None:
        # double linked list
        """ tmp = self.right.prev
        self.right.prev = Node(val)
        self.right.prev.next = self.right
        self.right.prev.prev = tmp
        tmp.next = self.right.prev """
        
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def addAtIndex(self, index: int, val: int) -> None:
        # double linked list
        """ if not index:
            self.addAtHead(val)
            return
        cur, i = self.left.next, 0
        while cur and i < index:
            cur = cur.next
            i += 1
        if cur:
            tmp = cur.prev
            cur.prev = Node(val)
            cur.prev.next = cur
            tmp.next = cur.prev
            cur.prev.prev = tmp """
        
        prev, i = self.head, 0 # prev is previous of required index
        while prev and i < index:
            prev = prev.next
            i += 1
        if prev and not prev.next: # update tail if element added at tail
            prev.next = Node(val)
            self.tail = prev.next
        elif prev:
            tmp = prev.next
            prev.next = Node(val)
            prev.next.next = tmp

    def deleteAtIndex(self, index: int) -> None:
        # double linked list
        """ cur, i = self.left.next, 0
        while cur and i < index:
            cur = cur.next
            i += 1
        if cur and cur != self.right:
            cur.prev.next = cur.next
            cur.next.prev = cur.prev """
        
        prev, i = self.head, 0 # prev is previous of required index
        while prev and i < index:
            prev = prev.next
            i += 1
        if prev and prev.next and not prev.next.next: # update tail if last element deleted
            self.tail = prev
            prev.next = None
        elif prev and prev.next:
            prev.next = prev.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

