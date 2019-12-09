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

    '''
    HOWARDS SOLUTION
    def remove(self, key):
        # removes the first node found with data that matches the given key value within the linked list
        if self.head.data == key:
            self.head = self.head.next
        else:
            curr = self.head
            while curr is not None and curr.data != key:
                prev = curr
                curr = curr.next
            if curr is not None:
                prev.next = curr.next
                #Howard doesn't believe the line below is required.
                curr.next = None
            else:
                print("Did not find an element with data", key)
    '''

    def delete_node(self,value):
        probe_list = []
        if self.head is None:
            return
        else:
            probe = self.head
            while probe is not None:
                probe_list.append(probe)
                probe = probe.next
            prev = None
            probe = self.head
            while probe is not None and probe.data is not value:
                prev = probe
                probe = probe.next
            if probe not in probe_list:
                print(f"{value} is not found in linked list.")
                return
            try:
                prev.next = probe.next
            except:
                self.head = probe.next

    def delete_index(self, index):
        if self.head is None:
            return
        else:
            probe = self.head
            if index <= 0:
                self.head = probe.next
            while probe.next is not None and index > 1:
                probe = probe.next
                index -= 1
            try:
                probe.next = probe.next.next
            except:
                print("Index is out of range!")


if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    llist.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    llist.delete_index(4)

    llist.print_list()