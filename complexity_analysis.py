'''
***********************Complexity ANAL-y-SIS***********************


complexity analysis - a method of determining the efficiency of algorithms that
                      allows you to rate them independently of platform-dependent
                      timings or impractical instruction counts


order of complexity - the difference in performance of your algorithms

linear - grows in direct proportion to the size of the problem

quadratic - grows as a function of the square of the problem size

logarithmic - proportional to the log base 2 of the problem size

polynomial time algorithm - grows at a rate of n raised to the k

exponential - a growth rate of 2 raised to the n. these are impractical
              to run with large problem sizes


*********************** Big-O Notation ***********************
*O stands for Order (Order of complexity)

Dominant - the term with an amount of work in an algorithm that becomes so large
           that you can ignore the amount of work represented by the other terms

           (1/2)n^2-(1/2)n
           n^2 is dominant

           Represented with Big-O notation
           O(n^2)


Constant O(1)
    - Time taken is independent of the amount of data
    - EX: Stack push, pop and peek; Queue, dequeue and enqueue; Insert a node into
      a linked list

Linear O(n)
    - Time taken is directly proportional to the amount of data
    - Linear search; Count items in a list; Compare a pair of strings

Quadratic O(n^2)
    - Time taken is proportional to the amount of data squared , twice as much
      data takes 4 times as long to process, poor scalability
    - EX: Bubble sort; Selection sort; Insertion sort; Traverse a 2D array

Polynomial O(n^k)
    - Time taken is proportional to the amount of data raised to the power of
      a constant

Logarithmic O(log n)
    - Time taken is proportional to the logarithm of the amount of data,
      good scalability
    - EX: Binary search a sorted list; Search a binary tree; Divide and conquer
      algorithm approaches

Linearithmic O(n log n)
    - Time taken is proprtional to the logarithm of the amount of data,
      multiplied by the amount of data

Exponential O(k^n)
    - Time taken is proportional to a constant raised to the power of the amount
      of data, very poor scalability almost immediately.
    - EX: If constant k is 10, then one extra item of data will slow it down
      by ten times

Logarithms - The inverse of exponentiation

    Generally
        x^z = y     ==      log base x of y = z

        EX:
        2^0 = 1     ==      Log base 2 of 1 = 0
        2^1 = 2     ==      Log base 2 of 2 = 1
        2^2 = 4     ==      Log base 2 of 4 = 2
        2^3 = 8     ==      Log base 2 of 8 = 3
        2^4 = 16    ==      Log base 2 of 16 = 4

        2^4=10,000  ==      Log base 10 of 10,000 = 4

        Notice that each number that we're calculating the log of is twice as much as
        the previous number but each log is only 1 bigger than the previous value



'''