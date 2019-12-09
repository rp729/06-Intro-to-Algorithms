'''
Running things concurrently is known as multithreading
Running things in parallel is known as multiprocessing

I/O bound tasks - Waiting for input ad output to be completed,
                    reading and writing from file system,
                    network operations
                    These all benefit more from threading
                    You get the illusion of running code at the same time,
                        however, other code starts running while other code
                        is waiting

cpu bound tasks - Good for number crunching / using CPU / data crunching
                    These benefit more from multiprocessing and running in parallel
                    Using multiprocessing might be slower if you have overhead from creating and
                    destroying files
'''
import multiprocessing
import time


def do_something():
    print("sleeping 1 seconds")
    time.sleep(1)
    print('Done Sleeping')

if __name__ == "__main__":
    start = time.perf_counter()
    #Create 2 threads
    p1 = multiprocessing.Process(target=do_something)
    p2 = multiprocessing.Process(target=do_something)

    #Start the thread
    p1.start()
    p2.start()

    # Make sure the threads complete before moving on to calculate  finish time
    p1.join()
    p2.join()

    finish = time.perf_counter()

    print(f'Finished in {finish-start} second(s)')
