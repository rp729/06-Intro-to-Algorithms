# Prints the nubmer of calls of a recursive Fibonacci
# function with problem sizes that double

from counter import Counter

def finb(n, counter):
    # Count the number of calls of the fib function
    counter.increment()
    if n < 3:
        return 1
    else:
        return fib(n - 1,counter) + fib(n - 2, counter)

    problemSize = 2
    for count in range(5):
        counter =