---
title: difference
tags: list,beginner
---

Returns the difference between two iterables.

- Use Python's set operator for difference to find all values in `a` that are not in `b`.

```py
def difference(a, b):
  return list(set(a) - set(b))
```

```py
difference([1, 2, 3], [1, 2, 4]) # [3]
```
