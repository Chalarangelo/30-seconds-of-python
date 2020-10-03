---
title: geometric progression
tags: math,beginner
---

Returns a list of numbers in the geometric progression starting with the given positive integer and up to the specified limit.

There general form of geometric sequence is a, ar, ar<sup>2</sup>, ar<sup>3</sup>, ar<sup>4</sup>, ...
<br> where r -> common ratio and a -> initial value

- Use `range` and `list` with the appropriate start, step and end values.

```py
def geometric_progression(a, r, lim):
  gp = []
  while a < lim:
    gp.append(a)
    a *= r
  return  gp
```

```py
geometric_progression(3, 2, 100) # [3, 6, 12, 24, 48, 96] 
```
