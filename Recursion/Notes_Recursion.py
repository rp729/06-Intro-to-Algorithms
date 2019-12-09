'''def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        print(n)
        return n*recursive_factorial(n-1)

num = recursive_factorial(996)

print(num)
'''
#New function of recursion
'''def main():
    numbers = [1,2,3,4,5,6,7,8,9]
    my_sum = range_sum(numbers,2,5)
    print("The sum of items 2 through 5 is ",my_sum)

def range_sum(num_list,start_index,end_index):
    if start_index > end_index:
        return 0
    else:
        return num_list[start_index]+range_sum(num_list,start_index+1,end_index)

main()'''

#Fibonacci
'''def main():
    print('The first 10 number in the')
    print('Fibonacci series are:')

    for number in range(10):
        print(fibonacci(number))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

main()'''

#Greatest common divisor
'''def main():
    num1 = int(input('Enter an integer: '))
    num2 = int(input('Enter another integer: '))

    print('The greatest common divisor of')
    print('the two numbers is',gcd(num1,num2))

def gcd(x,y):
    if x%y == 0:
        return y
    else:
        return gcd(y,x%y)

main()'''

#Chicken scratch
'''def gcd(num1,num2):
    max_num = lambda x,y : max([x,y]) if x != y else x
    min_num = lambda x,y : min([x,y]) if x != y else x
    max_n = max_num(num1,num2)
    min_n = min_num(num1,num2)
    if '''

#Towers of Hanoi
'''
Rules:
1) Only one disk may moved at a time
2) A disk cannot be placed on top of a smaller disc
3) All discs must be stored on a peg except while being moved
4) You must move all discs from the first peg to the third peg

This program simulates the Towers of hanoi game
'''
def main():
    #Setup initial values
    num_disc = 64
    from_peg = 1
    to_peg = 3
    temp_peg = 2
    move_discs(num_disc,from_peg,to_peg,temp_peg)
    print("All the discs are moved!")

def move_discs(num,from_peg,to_peg,temp_peg):
    if num > 0:
        move_discs(num -1,from_peg,temp_peg,to_peg)
        print('Move a disc from peg', from_peg, 'to peg', to_peg)
        move_discs(num - 1,temp_peg,to_peg,from_peg)

main()
