"""
Stacks
    Linear collections in which acess is completely restricted to just one end
        called the top
    LIFO - Last in first out protocol, think of dishes stacked at a buffet

    push - put items on the stack
    pop - remove the top item from the stack
    peek - examine the top element on the stack

    The stack type is not built into Python so we use a list to emulate
        an array-based stack

    We're going to use the list methods append  and pop
    It's possible to utilize other list methods such as insert, replace, and remove
        but that defeats the purpose of the spirit of the stack

"""

class Stack:
    def __init__(self):
        self.my_stack = []

    def push(self,item):
        self.my_stack.append(item)

    def get_stack(self):
        return self.my_stack

    def pop(self):
        return self.my_stack.pop()

    def is_empty(self):
        return self.my_stack == []

    def peek(self):
        if not self.is_empty():
            return self.my_stack[-1]


s = Stack()
'''
s.push("First in")
s.push("Next one")
print(s.get_stack())
s.pop()
print(s.get_stack())
s.push("HAM!")
s.push("Sandwich")
print(s.get_stack())
print(s.peek())
'''

"""
Use a stack to check whether or not a string has balanced usage of parenthesis
Example:
    Balanced = (), ()(), (({[]}))
    Unbalanced = ((), [{(]]]
    
"""

def is_match(p1,p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    else:
        return False

def is_paren_balanced(paren_string):
    s = Stack()
    # an initial flag
    is_balanced = True
    # keep track of where we are
    index = 0
    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        # is it an open paren?
        if paren in "([{":
            s.push(paren)
        #it's a closed paren
        elif paren in ")]}":
            top = s.pop()
            if not is_match(top,paren):
                is_balanced = False
        else:
            print("Not a paren")
        index += 1
    if s.is_empty() and is_balanced:
        return True
    else:
        return False


print(is_paren_balanced("a"))