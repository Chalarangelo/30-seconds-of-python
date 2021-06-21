---
title: bubble_sort
tags: algorithm,array,beginner
firstSeen: 2021-06-21T00:52:09+17:00
---

Sorts an array of numbers, using the bubble sort algorithm.

- Use a `for` loop to iterate over the elements of the passed array, terminating before the last element.
- Use a nested `for` loop to iterate over the segment of the array between `0` and `len(a) - i - 1`, swapping any adjacent out of order elements.

```python
def bubble_sort(a):
  for i in range(len(a)):
    for j in range(len(a) - i - 1):
      if a[j + 1] < a[j]:
        a[j], a[j + 1] = a[j + 1], a[j]
  return a
```

```python
bubble_sort([2, 1, 4, 3]) # [1, 2, 3, 4]
```
