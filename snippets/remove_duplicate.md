---
title: remove_duplicates
tags: list, beginner
---

Removes any repeated entry if there are duplicate values in a flat list.

- Use `set()` on the given list to remove duplicates, then again typecast it into `list`.

```py
def remove_duplicates(lst):
  return list(set(lst))
```

```py
x = [1, 2, 3, 4, 5, 5]
y = ['A', 'a', 'b', 'B']
remove_duplicates(x) # [1, 2, 3, 4, 5]
remove_duplicates(y) # ['b', 'B', 'A', 'a] This method of removing duplicates is case-sensitive for a list of characters.
```
