'''
​2. For problem size n, algorithms A and B perform n^2 and (1/2)n^2 + (1/2)n
instructions, respectively. Which algorithm does more work?

(1/2)n^2 + (1/2)n



Are there particular problem sizes for which one algorithm performs
significantly better than the other?

WRONG > Due to complexity,(1/2)n^2 + (1/2)n will take more work as the number grows larger

*LOWER NUMBERS* algorithms become nearly identical as n gets larger because n^2 is dominant


Are there particular problem sizes for which both algorithms perform
approximately the same amount of work?
if n = 0 and if n is extremely large
'''

n = 2
for i in range(1000000):
    print(f'n^2 = {n**2} : (1/2)n^2 + (1/2)n = {(1/2)*n**2 + (1/2)*n}')
    n+=1