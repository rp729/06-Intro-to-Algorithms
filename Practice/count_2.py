'''
2. Run the program you created in Exercise 1 using problem sizes of
    1000, 2000, 4000, 10,000, and 100,000. As the problem size doubles
    or increases by a factor of 10, what happens to the number of iterations?
'''

def main():
    problemSize = [1000, 2000, 4000, 10000, 100000]
    count_it(problemSize)

def count_it(problemSize):
    for i in problemSize:
        count = 0
        print(f'{i}:')
        while i > 0:
            i = i // 2
            count += 1
        print(f'{count} iterations')

main()