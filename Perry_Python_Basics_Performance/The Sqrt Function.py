"""
25/25 points. Well done.
"""


'''    (The sqrt function) Write a program that prints the following table
    using your knowledge of loops and the sqrt function in the math module.
    Make sure your table is neat by using print formatting methods we've learned.

​

        Number  Square Root
        0       0.0000
        1       1.0000
        2       1.4142
        ...
        18      4.2426
        20      4.4721'''
#Import math
import math

#Main function
def main():
    sqrt_func()

#Square root function
def sqrt_func():
    print(f'Number  Square Root')
    for i in range(1,21):
        #-15 is for spacing and .4f is for decimal point
        print(f'{i:}{math.sqrt(i):-15.4f}')

main()
