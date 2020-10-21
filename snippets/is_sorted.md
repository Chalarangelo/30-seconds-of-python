---
title: is_sorted
tags: list,tuple,beginner
---

Checks if a list or tuple is sorted in ascending or descending order.

- Returns ```1``` if list is sorted in ascending order.
- Returns ```-1``` if list is sorted in descending order.
- Returns ```0``` if list is not sorted.

```py
def is_sorted(lst):
  if all(lst[i] <= lst[i+1] for i in range(len(lst)-1)):
    return 1
  if all(lst[i] >= lst[i+1] for i in range(len(lst)-1)):
    return -1
  return 0  
```

```py
is_sorted(("Mon","Tue","Wed")) # 1
is_sorted((1,2,1,3)) # 0
is_sorted([3,2,1,1]) # -1
```
