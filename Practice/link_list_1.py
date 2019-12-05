"""
Core Exercises:

    1. Finish out your doubly and circular linked list to add more functionality
        - prepend
        - insert
        - delete
        - print
"""

class DoubleNode:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self,data):
        newNode = DoubleNode(data)
        if self.head is None:
            newNode.prev = None
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = self.tail.next
    def print_linked_list(self):
        probe = self.head
        while probe != None:
            print(probe.data)
            probe = probe.next
    '''Question 1: Add insert to doubly'''
    def prepend(self,data):
        # instantiate a new Node object
        newNode = DoubleNode(data)
        # anything in our linked list?
        if self.head is None:
            newNode.prev = None
            self.head = newNode
            self.tail = self.head
        else:
            newNode.next = self.head
            self.head = newNode
    '''Question 1: Add insert to doubly'''
    def insert(self,index,data):
        newNode = DoubleNode(data)
        if self.head is None:
            newNode.prev = None
            self.head = newNode
            self.tail = self.head
        elif index <= 0:
            newNode.next = self.head
            self.head = newNode
        else:
            probe = self.head
            while probe.next != None and index > 1:
                probe = probe.next
                index -= 1
            probe.next = DoubleNode(data,probe.next)
            if probe == self.tail:
                self.tail = probe.next
    '''Question 1: Add delete to doubly'''
    def delete(self,index):
        if self.head is None:
            pass
        elif index <= 0:
            remove_data = self.head
            self.head = self.head.next
        else:
            probe = self.head
            while index > 1 and probe.next.next != None:
                probe = probe.next
                index -= 1
            removedItem = probe.next
            if self.tail == removedItem:
                self.tail = self.tail.prev
            probe.next = probe.next.next
    def swap(self,index_1,index_2):
        if self.head is None or self.head.next is None or index_1 == index_2:
            pass
        else:
            i1 = index_1
            i2 = index_2
            probe_1 = self.head
            probe_2 = self.head
            while probe_1.next != None and index_1 > 0:
                probe_1 = probe_1.next
                index_1 -= 1
            while probe_2.next != None and index_2 > 0:
                probe_2 = probe_2.next
                index_2 -= 1
            self.insert(i1,probe_2.data)
            self.delete(i1+1)
            self.insert(i2,probe_1.data)
            self.delete(i2+1)

'''    def swap(self,index_1,index_2):
        if self.head is None or self.head.next is None or index_1 == index_2:
            pass
        elif index_1 <= 0:
            probe_1 = self.head
            probe_2 = self.head
            while index_2 > 1 and probe_2.next.next != None:
                probe_2 = probe_2.next
                index_2 -= 1

        elif index_2 <= 0:
            probe_1 = self.head
            probe_2 = self.head
        else:
            pass'''


class Node():
    def __init__(self,data,next=None):
        #Instantiates a Node with a default next of None
        self.data = data
        self.next = next

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




doubly_linked_list = DoublyLinkedList()
doubly_linked_list.append("Ham_5")
doubly_linked_list.insert(0,"Ham_2")
doubly_linked_list.insert(1,"Ham_3")
doubly_linked_list.insert(2,"Ham_4")
doubly_linked_list.prepend("Ham_1")
doubly_linked_list.append('Ham_6')
doubly_linked_list.swap(0,5)

doubly_linked_list.print_linked_list()
