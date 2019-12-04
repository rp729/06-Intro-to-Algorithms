#This file will test the Node class

from node import Node

head = None

# Add five nodes to the beginning of the linked structure
for count in range(1,6):
    head = Node(count,head)

# Print the contents of the structure
while head != None:
    print(head.data)
    head = head.next


"""
- One pointer, head, generates the linked structure. This pointer is manipulated
    in such a way that the most recently inserted item is always at the beginning
    of the structure
- When the data are displayed, they appear in teh reverse order of their insertion
- Also, when the data are displayed, the head pointer is reset to the next node, until
    the head pointer become none. Thus, at the en of this process, teh nodes are 
    effectively deleted from teh linked structure. They are no longer available to 
    the program and are recycled during the next garbage collection
"""