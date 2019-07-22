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

![image](https://user-images.githubusercontent.com/19671036/60617131-af1cc980-9d98-11e9-906b-9ef70afefe92.png)

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

![image](https://user-images.githubusercontent.com/19671036/60617222-e4291c00-9d98-11e9-9e12-9ea864aa530e.png)

---

**Sequential Search of List**

![image](https://user-images.githubusercontent.com/19671036/60617264-fc00a000-9d98-11e9-859c-92694ea4216d.png)

---

**Binary Search:**

![image](https://user-images.githubusercontent.com/19671036/60617299-120e6080-9d99-11e9-9fcc-a4dd318da59c.png)

---

**Comparing Data Items**

![image](https://user-images.githubusercontent.com/19671036/60617320-1cc8f580-9d99-11e9-8ba7-0fcfc7434aaf.png)

![image](https://user-images.githubusercontent.com/19671036/60617339-27838a80-9d99-11e9-89df-8a5a8e338369.png)

---

### Sort Algorithms

---

**Basic Sort Demo 1:**

![image](https://user-images.githubusercontent.com/19671036/60617371-35d1a680-9d99-11e9-985c-5c3701d73885.png)

---

**Selection Sort Algorithm**

![image](https://user-images.githubusercontent.com/19671036/60617391-42ee9580-9d99-11e9-8b8b-cc3bd69a9294.png)

![image](https://user-images.githubusercontent.com/19671036/60617418-4eda5780-9d99-11e9-9d1a-20d8501050a9.png)
 
 ---
 
**Bubble Sort Algorithms**

![image](https://user-images.githubusercontent.com/19671036/60617432-5a2d8300-9d99-11e9-98a7-244e41034f3f.png)

![image](https://user-images.githubusercontent.com/19671036/60617455-6addf900-9d99-11e9-9a18-8d3672d60a8d.png)

---

**Modified Bubble Sort function:**

![image](https://user-images.githubusercontent.com/19671036/60617492-7b8e6f00-9d99-11e9-888d-05bab253f342.png)

![image](https://user-images.githubusercontent.com/19671036/60617513-8517d700-9d99-11e9-8e66-f9458a2883c5.png)

---

**Insertion Sort Algorithms**

![image](https://user-images.githubusercontent.com/19671036/60617537-8ea13f00-9d99-11e9-87ea-6240c2e67d56.png)

![image](https://user-images.githubusercontent.com/19671036/60617557-99f46a80-9d99-11e9-92fb-0fedd5714f07.png)

---

# Quick Sort & Merge Sort Algorithms

---

**Quicksort:**

![image](https://user-images.githubusercontent.com/19671036/60617571-a1b40f00-9d99-11e9-9e51-38febdb14eb5.png)

---

**Implementation of Quicksort**

![image](https://user-images.githubusercontent.com/19671036/60617610-b0022b00-9d99-11e9-9ba8-b92037a77400.png)

![image](https://user-images.githubusercontent.com/19671036/60617640-be504700-9d99-11e9-94f1-59ab28110248.png)

---

**Merge Sort Examples**

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
