class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print_llist(self):
        probe = self.head
        while probe is not None:
            print(probe.data)
            probe = probe.next

    def insert_after(self,new_node,prev_node=None):
        if prev_node is None or self.head is None:
            self.prepend(new_node)
        else:
            new_node = Node(new_node)
            new_node.next = prev_node.next
            prev_node.next = new_node

    def insert_index(self,data,index=0):
        if index <= 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            probe = self.head
            while index > 1 and probe.next is not None:
                probe = probe.next
                index -= 1
            probe.next = Node(data,probe.next)

    def prepend(self,new_node):
        new_node = Node(new_node)
        new_node.next = self.head
        self.head = new_node

if __name__ == "__main__":
    llist = LinkedList()

    llist.head = Node(2)
    second = Node(3)
    third = Node(4)
    llist.head.next = second
    second.next = third
    llist.insert_after(1)
    llist.prepend(0)
    llist.insert_index(7,2)

    llist.print_llist()