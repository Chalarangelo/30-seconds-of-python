---
title: factorial_iterative
tags: math,intermediate
---

Calculates factorial of a number in iterative way.

- Uses iterative method to get factorial.
- Only uses int object. Anything else will throw Error.

```py
def factorial_it(n):
  fac = 1
  for i in range(n):
    fac = fac * (i+1)
  return fac
```

```py
factorial_it(5) # 120
```
