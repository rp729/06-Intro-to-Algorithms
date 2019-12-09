'''8. Ackermann’s Function
    Ackermann’s Function is a recursive mathematical algorithm that can be used to test how
    well a system optimizes its performance of recursion. Design a function ackermann(m, n),
    which solves Ackermann’s function. Use the following logic in your function:
        If m = 0 then return n  1
        If n = 0 then return ackermann(m - 1, 1)
        Otherwise, return ackermann(m - 1, ackermann(m, n - 1))
    Once you’ve designed your function, test it by calling it with small values for m and n.'''




'''Main function'''
def main():
    m = input("Enter a number: ")
    m = num_validation(m)
    n = input("Enter a number: ")
    n = num_validation(n)
    print(ackerman(m,n))

'''Ackerman function'''
def ackerman(m,n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackerman(m - 1, 1)
    else:
        return ackerman(m - 1, ackerman(m, n - 1))

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