---
title: all_unique
tags: list,beginner
---

Returns `True` if all the values in a list are unique, `False` otherwise.

- Use `set()` to keep track of elements seen while iterating.
- Use `in` for checking if an element exists in the set.
- If it exists return `False`, else return `True`.

```py
def all_unique(lst):
  seen = set()
  for val in lst:
    if val in seen:
      return False
    seen.add(val)
  return True
```

```py
x = [1, 2, 3, 4, 5, 6]
y = [1, 2, 2, 3, 4, 5]
all_unique(x) # True
all_unique(y) # False
```
