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

    def append_dl(self,data):
        data = Node(data)
        #Only reason self.tail would be None is if the list was never created
        if self.tail == None:
            self.head = data
            self.tail = data
        else:
            probe = self.tail
            probe.next = data
            data.prev = probe
            self.tail = data

    def insert_after(self,data,prev_node):
        if self.head == None:
            print("Linked list is broken or data does not exist.")
            return
        new_node = Node(data)
        probe = self.head
        prev_probe = None
        while probe is not None and probe.data is not prev_node:
            prev_probe = probe
            probe = probe.next
        if probe == None:
            print("Value not found in linked list.")
            return
        temp = probe.next
        probe.next = new_node
        new_node.prev = probe
        new_node.next = temp
        temp.prev = new_node
        if self.tail == probe:
            self.tail = new_node

    def prepend(self,data):
        probe = self.head
        new_node = Node(data,probe)
        probe.prev = new_node
        self.head = new_node



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
    dllist.append_dl(4)
    dllist.insert_after(5,1)
    dllist.prepend(12)

    #Test print functions
    dllist.print_list()
    dllist.print_reverse()
