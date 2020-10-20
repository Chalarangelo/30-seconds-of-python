---
title: max_element_index
tags: list,beginner
---

Returns the index of the element with the maximum value in a list.

- Use `max()` and `list.index()` to get the maximum value in the list and return its index.

```py
def max_element_index(arr):
  return arr.index(max(arr))
```

```py
max_element_index([51, 81, 92, 75, 100, 38, 5]) # 4
```
