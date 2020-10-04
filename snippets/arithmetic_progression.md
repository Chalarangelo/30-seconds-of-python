---
title: arithmetic_progression
tags: math,beginner
---

Returns a list of numbers in the arithmetic progression starting with the given positive integer and up to the specified limit.

- Use `range` and `list` with the appropriate start, step and end values.

```py
def arithmetic_progression(first, limit, diff):
  '''
  first - first element
  limit - upper limit
  diff - common difference
  '''
  return list(range(first, limit + 1, diff))
```

```py
arithmetic_progression(5, 25, 4) # [5, 9, 13, 17, 21, 24] 
```
