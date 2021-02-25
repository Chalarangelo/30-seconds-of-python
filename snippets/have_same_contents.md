---
title: have_same_contents
tags: list,intermediate
---

Checks if two lists contain the same elements regardless of order.

- Use `sorted()` to sort the lists.
- Return `True` if their content is equal otherwise return `False`

```py
def have_same_contents(a, b):
  return sorted(a) == sorted(b)
```

```py
have_same_contents([1, 2, 4], [2, 4, 1]) # True
```
