# This class will represent a sinly linked node

class Node():
    def __init__(self,data,next=None):
        #Instantiates a Node with a default next of None
        self.data = data
        self.next = next

#Just an empty link
node1 = None

#A node containing data and an empty link
node2 = Node("A",None)
node3 = Node("B",node2)
node4 = Node(None,None)


#print(node3.next)