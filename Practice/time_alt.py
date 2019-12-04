'''
3. The difference between the results of two calls of the function time.time()
    is an elapsed time. Because the operating system might use the CPU for part
    of this time, the elapsed time might not reflect the actual time that a
    Python code segment uses the CPU. Browse the Python documentation for an
    alternative way of recording the processing time, and describe how this
    would be done.
'''
import time

problemSize = 1000

for count in range(5):
    start = time.process_time()
    #The start of a the algorithm
    work = 1
    for j in range(problemSize):
        for k in range(problemSize):
            work += 1
            work -= 1
    #The end of the algorithm
    elapsed = time.process_time() - start
    print(f'{problemSize} - {elapsed}')
    problemSize *= 2