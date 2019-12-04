'''
1. The list method reverse reverses the elements in the list. Define a function named reverse that
reverses the elements in its list argument (without using the method reverse). Try to make this
function as efficient as possible, and state its computational complexity using big-O notation.

2. Python’s pow function returns the result of raising a number to a given power. Define a function
expo that performs this task and state its computational com-plexity using big-O notation. The first
argument of this function is the number, and the second argument is the exponent (nonnegative numbers only).
You can use either a loop or a recursive function in your implementation, but do not use Python’s ** operator
or pow function.
'''

import matplotlib.pyplot as plt
import numpy as np

#1
def reverse(my_list):
    return my_list[::-1]

test_list = [1,2,3,4,5,6,7,8,9]

print(reverse(test_list))

#O(n) due to linear complexity

#2
def to_the_power(num,exp_num):
    if exp_num == 0:
        return 1
    new_num = num
    for i in range(exp_num-1):
        new_num = new_num*num
    return new_num

print(to_the_power(2,3))

#O(n)

