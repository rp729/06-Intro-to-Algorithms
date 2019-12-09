'''
5. Recursive List Sum
    Design a function that accepts a list of numbers as an argument. The function should recursively
    calculate the sum of all the numbers in the list and return that value.
'''

'''Main function'''
def main():
    num_list = []
    len_list = input("Enter the number of integers you'd like to add to your list: ")
    len_list = num_validation(len_list)
    for i in range(len_list):
        i = input(f"({i+1} of {len_list}) Enter an integer: ")
        i = num_validation(i)
        num_list.append(i)
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