---
title: list_2d_to_1d
tags: list,beginner
---

Flattens a 2d list into a 1d list.

- The + operator acts by concatenation on lists.
- Flattens the list from left to right.
- You add starting items as the following argument ```[start_list]```

```py
def list_2d_to_1d(array, start):
  return sum(array, [])
```

```py
list_2d_to_1d([[1,2],[2,3]], []) # [1. 2. 2, 3]
list_2d_to_1d([[1,2],[2,3]], [8,9]) # [8, 9, 1. 2. 2, 3]
```
