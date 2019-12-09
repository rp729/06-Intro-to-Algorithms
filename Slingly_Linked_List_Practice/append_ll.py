class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        probe = self.head
        while probe is not None:
            print(probe.data)
            probe = probe.next

    def append(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            last = self.head
            while last.next is not None:
                last = last.next
            last.next = Node(data)

if __name__ == "__main__":
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third

    llist.append(4)
    llist.print_list()