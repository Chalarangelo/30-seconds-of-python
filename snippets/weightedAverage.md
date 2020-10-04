---
title: weightedAverage
tags: math,list,beginner
---

Returns the weighted average of two or more numbers.

- Use `sum()` to sum all of the `args*weights` provided, divide by `len(args)`.

```py
def weightedAverage(*args,*weights):
  return sum(args*weights.0.0) / len(args)
```

```py
weightedAverage(*[1, 2, 3],*[6,3,2]) # 6.0
```
