"""
1. Write a tester program that counts and displays the number of iterations
    of the following loop:

    while problemSize > 0:
        problemSize = problemSize // 2
"""

def main():
    problemSize = 1000000
    count_it(problemSize)

def count_it(problemSize):
    count = 0
    while problemSize > 0:
        problemSize = problemSize // 2
        print(f'{problemSize} - {count}')
        count += 1

main()