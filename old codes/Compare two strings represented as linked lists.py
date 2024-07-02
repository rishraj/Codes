class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node


def compare(curr1, curr2):
    while curr1 is not None and curr2 is not None:
        if ord(curr1.data) < ord(curr2.data):
            print('-1')
            return
        elif ord(curr1.data) > ord(curr2.data):
            print('1')
            return
        else:
            curr1 = curr1.next
            curr2 = curr2.next

    if curr1 is None and curr2 is None:
        print('0')
    elif curr1 is None:
        print('-1')
    else:
        print('1')


str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")
llist1 = LinkedList()
llist2 = LinkedList()
for i in str1:
    llist1.add_node(i)
for i in str2:
    llist2.add_node(i)
compare(llist1.head, llist2.head)
