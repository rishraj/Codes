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

    def print_node(self):
        curr = self.head
        while curr.next is not None:
            print(str(curr.data)+'->', end='')
            curr = curr.next
        print(curr.data)

    def delete_node(self, data):
        if self.head.data == data:
            self.head.data = self.head.next.data
            self.head.next = self.head.next.next

        else:
            curr = self.head
            prev = curr
            while curr.data != data:
                prev = curr
                curr = curr.next

            prev.next = curr.next
            curr = None


llist = LinkedList()

llist.add_node(3)
llist.add_node(2)
llist.add_node(6)
llist.add_node(5)
llist.add_node(11)
llist.add_node(10)
llist.add_node(15)
llist.add_node(12)
llist.print_node()
llist.delete_node(5)
llist.print_node()
llist.delete_node(12)
llist.print_node()