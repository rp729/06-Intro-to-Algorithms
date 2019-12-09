class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    #Simple print statement
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    #Simple prepend function
    def prepend(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

if __name__ == "__main__":
    #Initialize the linked list
    llist = LinkedList()

    #Create nodes
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    #Establish links
    llist.head.next = second
    second.next = third
    llist.prepend(0)

    #print the list
    llist.print_list()