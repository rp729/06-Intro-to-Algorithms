class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def print_list(self):
        probe = self.head
        while probe is not None:
            print(probe.data)
            probe = probe.next

    def print_reverse(self):
        probe = self.tail
        while probe is not None:
            print(probe.data)
            probe = probe.prev

            #Below is Howard's reverse method
            '''
            temp = probe.next
            probe.next = probe.prev
            probe.prev = temp
            probe = probe.next
            '''

if __name__ == "__main__":
    #Initialize
    dllist = DoublyLinkedList()

    #Assign node values
    first = Node(1)
    second = Node(2)
    third = Node(3)

    #Link list together
    dllist.head = first
    first.next = second
    second.next = third
    second.prev = first
    third.prev = second
    dllist.tail = third

    #Test print functions
    dllist.print_list()
    dllist.print_reverse()
