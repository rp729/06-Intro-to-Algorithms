class Node:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_list(self):
        probe = self.head
        while probe is not None:
            print(probe.data)
            probe = probe.next

    def print_reversed(self):
        probe = self.tail
        while probe is not None:
            print(probe.data)
            probe = probe.prev

    def delete_item(self,value):
        if self.head is None:
            return
        probe = self.head
        while probe.data is not value:
            probe = probe.next
        try:
            probe.prev.next = probe.next
        except:
            pass
        try:
            probe.next.prev = probe.prev
        except:
            pass
        if probe == self.head:
            self.head = probe.next
        if probe == self.tail:
            self.tail = probe.

    def delete_index(self,index):
        if self.head == None:
            return
        probe = self.head
        if index <= 0:



if __name__ == "__main__":
    dllist = DoubleLinkedList()
    first = Node(1)
    dllist.head = first
    second = Node(2,None,first)
    first.next = second
    third = Node(3,None,second)
    second.next = third
    dllist.tail = third
    dllist.delete_item(2)

    dllist.print_list()
    dllist.print_reversed()