'''
3. Recursive Lines
    Write a recursive function that accepts an integer argument, n. The function should display
    n lines of asterisks on the screen, with the first line showing 1 asterisk, the second line
    showing 2 asterisks, up to the nth line which shows n asterisks.
'''

'''Main function'''
def main():
    num = input("Enter a number :")
    num = num_validation(num)
    asterick(num)

'''Where the magic happens'''
def asterick(num,ast=['*']):
    if num == 0:
        return num
    else:
        print(''.join(ast))
        ast.append('*')
        asterick(num-1,ast)

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