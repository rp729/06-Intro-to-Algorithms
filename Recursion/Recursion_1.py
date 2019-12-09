'''1. Recursive Printing
    Design a recursive function that accepts an integer argument, n, and prints the numbers 1
    up through n.'''

'''Main function'''
def main():
    num = input("Enter a number: ")
    num = num_validation(num)
    list_numbers(num,1)

'''Runs under main function'''
def list_numbers(num1,num2=1):
    if num1 == 0:
        return num1
    elif num2 <= num1:
        print(num2)
        return list_numbers(num1,num2+1)

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

'''Main'''
main()