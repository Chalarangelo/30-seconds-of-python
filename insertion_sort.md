---
title: insertion_sort
tags: list,intermediate
---

Uses Insertion Sort to sort numerical arrays. Insertion Sort has a time complexity of O(n^2) (worst case = n*(n-1)/2 inversions) and is generally faster than quicksort and mergesort.

- Use `[1:]` and `[:-1]` to compare all the values in the given list.

```py
def insertion_sort(lst):
  for i in range(len(lst)):
    b, c = lst[i], i-1
    while c >=0 and b < lst[c]:
      lst[c+1] = lst[c]
      c -= 1
    lst[c+1] = b
   return lst
```

```py
insertion_sort([-1, 0, 2, 5]) # [-1, 0, 2, 5]
insertion_sort([9, 9, -3, -8]) # [-8, -3, 9, 9]
```
