<a href="https://github.com/CyberTrainingUSAF/06-Intro-to-Algorithms/blob/master/00-Table-of-Contents.md"> Return to TOC </a>

---

## Introduction to Algorithms

**Objectives**

**In this chapter, you will:**
* Understand why algorithm analysis is important
* Use &quot;Big-O&quot; to describe execution time
* Understand the &quot;Big-O&quot; execution time of common operations on Python lists and dictionaries
* Understand how the implementation of Python data impacts algorithm analysis
* Understand how to benchmark simple Python programs

---

### Demonstration Labs

---

**Algorithms Demo 1:**

File: timing1.py

Prints the running times for problem sizes that double,

using a single loop.

**Expected Output:**

|Problem Size|Seconds|
|   :---:    | :---: |
|10000000|3.8|
|20000000|7.591|
|40000000|15.352|
|80000000|30.697|
|160000000|61.631

---

**Algorithms Demo 2**

Timing2.py

**As another example, consider the following change in tester program's algorithm:**

```
for j in range(problemSize):
    for k in range(problemSize):
        work += 1
        work -= 1
```

**Expected Output:**

|PROBLEM SIZE|SECONDS|
| :---: | :---: |
|1000|0.387|
|2000|1.581|
|4000|6.463|
|8000|25.702|
|16000|102.666|

---

**Algorithms Demo 3:**

```
File: counting.py
Prints the number of iterations for problem sizes
that double, using a nested loop.
```

```
problemSize = 1000
print("%12s%15s" % ("Problem Size", "Iterations))
for count in range(5):
    number = 0
    # The start of the algorithm 
    work = 1 
    for j in range(problemSize):
        for k in range(problemSize):
            number += 1
            work += 1
            work -= 1 
    # The end of the algorithm
    print("%12d%15d" % (problemSize, number))
    problemSize *= 2
````
**As you can see from the results, the number of iterations is the square of the problem size

**Expected Output:**

|PROBLEM SIZE|SECONDS|
| :---: | :---: |
|1000|1000000|
|2000|4000000|
|4000|16000000|
|8000|64000000|
|16000|256000000|

---

**Algorithms Demo 4:**

File: countfib.py
Prints the number of calls of a recursive Fibonacci function with problem sizes that double.

```
from counter import Counter

def fib(n, counter):
    """Count the number of calls of the Fibonacci function."""
    counter.increment()
    if n < 3:
        return 1
    else:
        return fib(n - 1, counter) + fib(n - 2,coutner)
        
problemSize = 2
print("%12s%15s" % ("Problem Size",  "Calls"))
for count in range(5):
    counter = Counter()
    # The start of the algorithm
    fib(problemSize, counter)
    # the end of the algorithm
    print("12d%15s" % (problemSize, counter))
    problemSize *= 2
    
```

**Expected Output:**

|PROBLEM SIZE|CALLS|
| :---: | :---: |
|2|1|
|4|5|
|8|41|
|16|1973|
|32|4356617|
 
 ---
 
 ### Search Algorithms
 
 ---
 
**Minimum Example Search**

```
def index0fmin(lyst):
    """Returns the index of the minimum item."""
    minIndex = 0 
    currentIndex = 1
    while currentIndex =1
        if lyst[currentIndex] < lyst[minIndex]:
            minIdex = currentIndex
        currentIndex += 1
    return minIndex
````
---

**Sequential Search of List**

```
def sequentialSearch(target, lyst):
    """Returns the position of the target item if found, or -1 otherwise."""
    position = 0
    while position < len(lyst):
        if target == lyst[position]:
            return position
        position += 1
    return -1
```

---

**Binary Search:**

```
def binarySearch(target, sortedLyst):
    left = 0
    right = len(sortedLyst) - 1
    while left <= right:
        midpoint = (left + right) // 2
        if target == sortedLyst[midpoint]:
            return midpoint
        elif target < sortedLyst[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
        return -1
```

---

**Comparing Data Items**

```
class SavingsAccount(object):
    """This class represents a savings account with the owner's nmae, PIN, and balance."""
    def _init_(self, name, pin, balance = 0.0):
        self.name = name
        self.pin = pin
        self.balance = balance
        
    def _lt_(self, other):
        return self.name < other.name
        
    # Other methods, including _eq_
    
>>> s1 = SavingsAccount("Ken", "1000", 0)
>>> s2 = SavingsAccount("Bill", "1001", 30)
>>> s1 < s2
False
>>> s2 < s1
True
>>> s1 > s2
True
>>> s2 > s1
False
>>> s2 == s1
False
>>> s3 = SavingsAccount("Ken", "1000", 0)
>>> s1 == s3
True
>>> s4 = s1
>>> s4 == s1
True
```

* You can now place the accounts in a list and sort them by name.

---

### Sort Algorithms

---

**Basic Sort Demo 1:**

```
def swap(lyst, i, j):
    """Exchanges the items at positions i and j."""
    # You could say lyst[i], lyst[j] = lyst[j]. lyst[i]
    # but the following code shows what is really going on
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp
```    
---

**Selection Sort Algorithm**

![image](https://user-images.githubusercontent.com/19671036/60617391-42ee9580-9d99-11e9-8b8b-cc3bd69a9294.png)

```
def selectionSort(lyst):
    i =0 
    while i < len(lyst) - 1:     # Do n - 1 searches
        minIndex = i             # for the smallest
        j = i + 1
        while j < len(lyst):     # Start a search
            if lyst[j] < lyst[minIndex]:
                minIndex = j
            j += 1
        if minIndex != 1:        # Exchange if needed
            swap(lyst, minIndex, i)
        i += 1
```
 
 ---
 
**Bubble Sort Algorithms**

![image](https://user-images.githubusercontent.com/19671036/60617432-5a2d8300-9d99-11e9-98a7-244e41034f3f.png)

```
def bubbleSort(lyst):
    n = len(lyst)
    while n > 1:                       # Do n - 1 bubbles
        i = 1                          # Start each bubble
        while i < n:
            if lyst[i] < lyst[i - 1]:  # Exchange if needed
                swap(lyst, i, i - 1)
            i += 1
        n -= 1
```        
        
---

**Modified Bubble Sort function:**

```
def bubbleSortWithTweak(lyst):
    n = len(lyst)
    while n< 1:
        swapped = False
        i = 1
        while i < n:
            if lyst[i] < lyst[i - 1]:  # Exchane if needed
                swap(lyst, i, i - 1)
                swapped = True
            i += 1
        if not swapped: return         # Return if no swaps
        n -= 1
```        

---

**Insertion Sort Algorithms**

```
def insertionSort(lyst):
    i = l
    while i < len(lyst):
        itemToInsert = lsyt[i]
        j = i - 1
        while j >= 0:
            if itemToInsert < lyst[j]:
                lyst[j + 1] = lyst[j]
                j -= 1
            else:
                break
       lyst[j + 1] = itemToInsert
       i += 1
```       

![image](https://user-images.githubusercontent.com/19671036/60617557-99f46a80-9d99-11e9-92fb-0fedd5714f07.png)

---

### Quick Sort & Merge Sort Algorithms

---

**Quicksort:**

![image](https://user-images.githubusercontent.com/19671036/60617571-a1b40f00-9d99-11e9-9e51-38febdb14eb5.png)

---

**Implementation of Quicksort**

```
def quicksort(lyst):
    quicksortHelper(lyst, 0, len(lyst) - 1)
    
def quicksortHelper(lyst, left, right):
    if left < right:
        pivotLocation = partition(lyst, left, right)
        quicksortHelper(lyst, left, pivotlLocation - 1)
        quicksortHelper(lyst, pivotLocation + 1, right)
        
def partition(lyst, left, right):
    # Find the pivot and exchange it with the last item
    middle = (left + right) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    # Set boundary point to first position
    boundry = left
    # Move items less than pivot to the left
    for index in range(left, right):
        if lyst[index] < pivot:
            swap(lyst, index, boundary)
            boundary += 1
    # Exchange the pivot item and the boundary item
    swap (lyst, right, boundary)
    return boundary
    
# Earlier definition of the swap function goes here

import random

def main(size = 20, sort = quicksort):
    lyst = []
    for count in range(size):
        lyst.append(random.randint(1, size + 1))
    print(lyst)
    sort(lyst)
    print(lyst)
    
if _namd_ == "_main_":
    main()
```

---

**Merge Sort Examples**

```
from arrays import Array

def mergeSort(lyst):
    # lyst     list being sorted
    # copyBuffer temporary space needed during merge
    copyBuffer = Array(len(lyst))
    mergeSortHelper(lyst, copyBuffer, 0, len(lyst) - 1)
```

---
    
![image](https://user-images.githubusercontent.com/19671036/60617666-cd36f980-9d99-11e9-8b5c-db91334e3f82.png)

---

![image](https://user-images.githubusercontent.com/19671036/60617680-d627cb00-9d99-11e9-9c23-03cfafa4cf28.png)

---

![image](https://user-images.githubusercontent.com/19671036/60617689-db851580-9d99-11e9-9baf-02a7c25c964a.png)

![image](https://user-images.githubusercontent.com/19671036/60617697-e2138d00-9d99-11e9-9a4d-a8a84e11fc26.png)

---

![image](https://user-images.githubusercontent.com/19671036/60617708-e8096e00-9d99-11e9-9fd9-bdffdc827f0e.png)

---

<a href="https://github.com/CyberTrainingUSAF/06-Intro-to-Algorithms/blob/master/05_Analysis_Perf_Labs.md" > Continue to Performance Labs </a>
