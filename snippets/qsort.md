---
title: qsort
tags: array,list,intermediate
---

Quicksort is an algorithm used to quickly sort items within an array no matter how big the array is. 
It is quite scalable and works relatively well for small and large data sets, and is easy to implement 
with little time complexity. It does this through a divide-and-conquer method that divides a single large array 
into two smaller ones and then repeats this process for all created arrays until the sort is complete.

```py
def qsort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr.pop()
    greater, lesser = [], []
    for item in arr:
        if item > pivot:
            greater.append(item)
        else:
            lesser.append(item)
    return qsort(lesser) + [pivot] + qsort(greater)
```

```py
qsort([5, 4, 3, 5, 4, 3]) # [3, 3, 4, 4, 5, 5]
qsort([5, -1]) # [-1, 5]
```