'''
2. Recursive Multiplication
    Design a recursive function that accepts two arguments into the parameters x and y. The
    function should return the value of x times y. Remember, multiplication can be performed
    as repeated addition as follows:
    7 X 4 = 4 + 4 + 4 + 4 + 4 + 4 + 4
    (To keep the function simple, assume that x and y will always hold positive nonzero
    integers.)
'''

'''Main function'''
def main():
    num_list = []
    num1 = input("Enter a number: ")
    num1 = num_validation(num1)
    num2 = input("Enter a number: ")
    num2 = num_validation(num2)
    multiply_list = multiply(num1,num2,num_list)
    print(num1,' X ',num2,' = ',' + '.join(multiply_list))

'''Where the magic happens'''
def multiply(num1,num2,num_list):
    if num1 == 0 or num2 == 0:
        return 0
    elif len(num_list) < num1:
        num_list.extend([str(num2)])
        return multiply(num1,num2,num_list)
    else:
        return num_list

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