#This prints the running times for problem sizes that double,
#Using a single loop

import time

problemSize = 1000

for count in range(5):
    start = time.time()
    #The start of a the algorithm
    work = 1
    for j in range(problemSize):
        for k in range(problemSize):
            work += 1
            work -= 1
    #The end of the algorithm
    elapsed = time.time() - start
    print(f'{problemSize} - {elapsed}')
    problemSize *= 2