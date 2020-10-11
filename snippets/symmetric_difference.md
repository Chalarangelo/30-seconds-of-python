---
title: symmetric_difference
tags: list,beginner
---

Returns the symmetric difference between two iterables, without filtering out duplicate values.

- Use the built-in symmetric difference operator that Python sets provide.

```py
def symmetric_difference(a, b):
  return list(set(a) ^ set(b))
```

```py
symmetric_difference([1, 2, 3], [1, 2, 4]) # [3, 4]
```
