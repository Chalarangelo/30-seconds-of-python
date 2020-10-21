---
title: heap_sort
tags: sort,algorithm
---

Method that implement heap sort algorithm.

- Use `heap_sort(param)` where `param` is a variable of list type and this method will to implement 
the Heap sort algorithm.

```py
def heapify(nums, heap_size, root_index):
    """
    Method that heapify the algorith.
    """

    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)

def heap_sort(nums):
    """
    Method that implement heap sort algorithm.
    """

    n = len(nums)

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
```

```py
param = [33, 13, 42, 8, 51]
heap_sort(param)
```
