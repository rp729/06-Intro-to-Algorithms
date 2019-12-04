'''
1. Suppose that a list contains the values 20, 44, 48, 55, 62, 66, 74, 88, 93, 99
at index positions 0 through 9. Trace the values of the variables left, right, and
midpoint in a binary search of this list for the target value 90. Repeat for the
target value 44.
'''

def binary_search(target,my_list):
    left = 0
    right = len(my_list)
    while left <= right:
        midpoint = (left + right) // 2
        if target == my_list[midpoint]:
            return midpoint
        elif target < my_list[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return "IDi0T! ThAt # iz knot en lIsT"

my_list = [20, 44, 48, 55, 62, 66, 74, 88, 93, 99]

print(binary_search(90,my_list))