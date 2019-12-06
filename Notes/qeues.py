"""
Queues
    A linear collection that adds elements to one end and removes them from
        the other in a FIFO {1st in 1st out} protocol
    Qeues are implemented in an many ways, some based on arrays, and some based
        on lists

    rear - insertions are restricted this end
    front - removals are restricted to this end

    Two fundamental operations, add and pop
        add - adds item to the rear
        pop - removes item from the front
        peek - see the item at the front of the queue


    There are priority queues that schedule their elements using a rating scheme
    as well as FIFO. If two elements have same rating then they are scheduled in
    FIFO order. Elements are ranked from smallest to largest according to some
    attribute lik a number or char, generally smallest are removed first no
    matter when thehy are added to the queue. (Dijkstra's shortest path algorithm)
"""

class Queue:
    def __init__(self):
        self.queue = []

    def push(self):
        item = input("What item would you like to push?")
        self.queue.append(item)

    def pop(self):
        item = self.queue.pop(0)
        print("You popped ", item)

    def peek(self):
        if self.queue:
            print(self.queue[0])

    def view_q(self):
        for i in range(len(self.queue)):
            print(f'Item {i} is {self.queue[i]}')


q = Queue()

while True:
    print("-----------------------------")
    print("Queue Options")
    print("1. View Queue\n2. See next in Queue\n3. Push onto the Queue\n4. Pop out of the Queue")
    print("-----------------------------")

    menu_choice = int(input("Enter your option:"))
    print()

    if menu_choice == 1:
        q.view_q()
    if menu_choice == 4:
        q.peek()
    if menu_choice == 3:
        q.push()
    if menu_choice == 4:
        q.pop()
