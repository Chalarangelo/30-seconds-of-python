---
title: buble
tags: sort,beginner
---

Implements a bubble sort on a given array.

- Compares adjacent elements and swaps them if necessary
- Repeats until the list is sorted
- [Wikipedia](https://en.wikipedia.org/wiki/Bubble_sort)

```py
def bubbleSort(arr): 
    n = len(arr) 
  
    for i in range(n): 
      for j in range(0, n-i-1): 
        if arr[j] > arr[j+1] : 
          arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr

```

```py
array = [3, 2, 6, 4, 1, 5]
bubleSort(array) # result
```
