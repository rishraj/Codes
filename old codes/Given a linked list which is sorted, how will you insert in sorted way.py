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
            new_node.next = self.head
            self.head = new_node

    def add_element(self, data):
        curr = self.head
        new_node = Node(data)
        prev = curr
        while curr.data <= new_node.data:
            prev = curr
            curr = curr.next
        new_node.next = curr
        prev.next = new_node

    def print_list(self):
        curr = self.head
        while curr.next is not None:
            print(str(curr.data) + '->', end='')
            curr = curr.next
        print(curr.data)


llist = LinkedList()
llist.add_node(15)
llist.add_node(10)
llist.add_node(7)
llist.add_node(5)
llist.add_node(2)
llist.print_list()
llist.add_element(9)
llist.print_list()