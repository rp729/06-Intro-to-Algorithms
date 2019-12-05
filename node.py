# This class will represent a sinly linked node

class Node():
    def __init__(self,data,next=None):
        #Instantiates a Node with a default next of None
        self.data = data
        self.next = next

'''#Just an empty link
node1 = None

#A node containing data and an empty link
node2 = Node("A",None)
node3 = Node("B",node2)
node4 = Node(None,None)


#print(node3.next)'''


# This LinkedList class will instantiate Node objects and we'll add methods
# to this class to add functionality
class LinkedList:
    def __init__(self):
        self.head = None
        # printing our linked list
    def print_linked_list(self):
        probe = self.head
        while probe != None:
            print(probe.data)
            probe = probe.next
    # add things to our linked list
    def append(self,data):
        # instantiate a new Node
        newNode = Node(data)
        # is there something in our linked list yet?
        if self.head is None:
            self.head = newNode
        # there are node(s) in our linked list
        else:
            probe = self.head
            while probe.next != None:
                probe = probe.next
            probe.next = newNode
    def prepend(self,data):
        # instantiate a new Node object
        newNode = Node(data)
        # anything in our linked list?
        newNode.next = self.head
        self.head = newNode
    def insert_node(self,index,data):
        if self.head is None or index <= 0:
            self.head = Node(data, self.head)
        else:
            probe = self.head
            while index > 1 and probe.next != None:
                probe = probe.next
                index -= 1
            probe.next = Node(data,probe.next)
    def delete_node(self,index):
        # Is this the only node?
        if index <= 0 or self.head.next is None:
            removedItem = self.head.data
            self.head = self.head.next
        else:
            probe = self.head
            while index > 1 and probe.next.next != None:
                probe = probe.next
                index -= 1
            removedItem = probe.next.data
            probe.next = probe.next.next





'''

linked_list = LinkedList()
linked_list.append("b")
linked_list.append("because, I can!")
linked_list.append("xyz")
linked_list.append("HAM!")
linked_list.prepend("I should be at the beginning... HAM!")
linked_list.insert_node(12,"inserted")
linked_list.delete_node(1)

linked_list.print_linked_list()'''


'''
Circular Linked List - Special case of singly linked list
                        Insertion and removal of the first node are special cases of the insert ith
                        and remove ith operations on a singly linked list. These are special
                        because the head pointer must be reset. You can use circular linked lists
                        with a dummy header node. Contains a link from the last node back to
                        the first node in the structure.
'''

class CircularLinked:
    def __init__(self):
        self.head = None

    def append(self,data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            newNode = Node(data)
            probe = self.head
            while probe.next != self.head:
                probe = probe.nenxt
            probe.next = newNode
            newNode.next = self.head