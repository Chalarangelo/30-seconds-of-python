---
title: binary_search
tags: algorithm, intermediate
---

Returns the index of the element to be searched in the array

bisect is an inbuilt library in python that is used to find the index of the element in O(logn) time complexity. This module provides support for maintaining a list in sorted order without having to sort the list after each insertion.

```py

import bisect
def binary_search(arr,value_to_search):
  return bisect.bisect(arr, value_to_search)

```

```py

binary_search([1, 5, 9, 15, 22, 67, 98], 15)  # 4
binary_search([1, 5, 9, 15, 22, 67, 98], 1)  # 1

```
