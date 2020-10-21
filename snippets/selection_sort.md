---
title: selection_sort
tags: sort,algorithm
---

Method that implement selection sort algorithm.

- Use `selection_sort(param)` where `param` is a variable of list type and this method will to implement 
the Selection sort algorithm.

```py
def selection_sort(nums):
    """
    Method that implement selection sort.
    """

    for i in range(len(nums)):
        lowest_value_index = i

        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j

        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
```

```py
param = [13, 8, 4, 22, 11]
selection_sort(param)
```
