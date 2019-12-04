'''
collection - a group of zero or more items that can be treated as a conceptual unit.
             Things like strings, lists, tuples dictionaries

             other types of collections include stacks, queus, priority qeues,
             binary search trees, heaps, graphs, and bags


Linear collection - like people in a line, they're ordered by position
                    each item except the first has a unique predecessor

                    Ex: Grocery lists, stacks of dinner plates, and a line at the atm



Hierarchical collection - ordered in a structure resembling an upside down tree.
                          Each data item except the one at the top has just one
                          predecessor called its parent, but potentially has many
                          successors called children.

                          Ex: file directory system, a company's organization tree, and
                          a book's table of contents


Graph collection - Also just called graph. Each item can have many predecessors and many
                   successors. AKA neighbors

                   Ex: Airline routes between cities, electrical wiring diagrams, internet


Unordered collections - These are not in a ny particular order, and it's not possible to
                        meaningfully speak of an item's predecessor or successor.

                        Ex: A bag of marbles

_________________________________________________________________________________
*********************************OPERATION TYPES*********************************
---------------------------------------------------------------------------------


Test for item membership - Use Python's in operator to search for a given target
                           Returns True if the item is found and False otherwise


Traverse the collection - Use Python's for loop to visit each item in the collection.
                          The order which items are visited depends upon the type of
                          collection.


Obtain a string representation - Use Python's str function to obtain the string
                                 representation of the collection.


Test for equality - Use Python's == operator to determine whether two collections are equal
                    if they are of the same type and contain the same items. The order in which
                    pairs of items are compared depends on the type of collection.


Concatentate two collections - Use Python's + operator to obtain a new collection of the same
                               type as the operands, and containing the items in the two operands.


Convert to another type of collection - Create a new collection with the same items as a source
                                        collection.


Insert an item - Add the item to the collection, possibly at a given position

Remove an item - Remove the item from the collection, possibly at a given position

Replace an item - Combine removal and insertion into one operation

Access or retrieve an item - Optain an item, possibly at a given position

'''