'''
Doubly linked lists - Very similar to singly linked; however, these have prev pointer
                        and a tail node.
                        Move left, to previous node, from a given node
                        Move immediately to the last node
'''

class DoubleNode:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def print_linked_list(self):
        probe = self.head
        while probe != None:
            print(probe.data)
            probe = probe.next
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



doubly_linked_list = DoublyLinkedList()
doubly_linked_list.append("first node's data")

doubly_linked_list.print_linked_list()
