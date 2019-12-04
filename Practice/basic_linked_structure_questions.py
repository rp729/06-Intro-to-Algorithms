"""
1. Using box and pointer notation, draw a picture of the nodes created by the
first loop in the tester program.

link_structure_diagram.png

2. What happens when a programmer attempts to access a node’s data fields when
the node variable refers to None? How do you guard against it?

You get an attribute error, while loop (ex: while head != None)

3. Write a code segment that transfers items from a full array to a singly linked
structure. The operation should preserve the ordering of the items.

testnode.py is single linked structure
"""

from node import Node

head = None

i = len(array) - 1

while i > 0:
    head = Node(array[i],head)
    i -=1

