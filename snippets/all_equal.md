---
title: all_equal
tags: list,beginner
---

Check if all elements in a list are equal.

```py
def all_equal(lst):
    for i in lst:
        if lst[0] != i:
            return False
    return True
```

```py
all_equal([1, 2, 3, 4, 5, 6]) # False
all_equal([1, 1, 1, 1]) # True
```
