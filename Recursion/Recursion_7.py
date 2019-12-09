'''7. Recursive Power Method
    Design a function that uses recursion to raise a number to a power. The function should
    accept two arguments: the number to be raised and the exponent. Assume that the exponent is a
    nonnegative integer.'''

'''Main Function'''
def main():
    num = input("Enter a number:")
    num = num_validation(num)
    num2 = num
    exp = input("Enter exponent:")
    exp = num_validation(exp)
    recursive_power(num,num2,exp)

'''Finds the exponent of any number using recursion'''
def recursive_power(num,num2,exp):
    exp -= 1
    if exp == 0:
        print(num)
        return 0
    else:
        num = num*num2
        recursive_power(num,num2,exp)

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