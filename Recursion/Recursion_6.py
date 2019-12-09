'''
6. Sum of Numbers
    Design a function that accepts an integer argument and returns the sum of all the integers from 1 up
    to the number passed as an argument. For example, if 50 is passed as an argument, the function will
    return the sum of 1, 2, 3, 4, . . . 50. Use recursion to calculate the sum.
'''

'''Main function'''
def main():
    num_list = []
    num = input("Enter the number you'd like to sum: ")
    num = num_validation(num)
    for i in range(num):
        num_list.append(i+1)
    recursive_sum(num_list)

'''Where the magic happens'''
def recursive_sum(num,sum=0):
    if len(num) == 0:
        print(sum)
    else:
        sum += num[0]
        num.pop(0)
        recursive_sum(num,sum)

'''Simple input validati0n'''
def input_validation(num):
    while str.isnumeric(num) == False:
        num = input("INVALID INPUT! Enter a number: ")
    return int(num)
def num_validation(num):
    num = input_validation(num)
    while num >= 996:
        num = input("INVALID INPUT! Must be less than 996: ")
        num = input_validation(num)
    return num


main()