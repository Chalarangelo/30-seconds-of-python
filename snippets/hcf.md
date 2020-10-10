---
title: hcf
tags: loop,list,intermediate
---

Returns the highest common factor of two numbers.

- This funtion is based on the Euclidean algorithm—the H.C.F. of two numbers divides their difference as well.
- Inside the `while` function the values `a` and `b` are swapped with `b` and and `a % b` (their difference)
- The value of `a` when `b` (`a % b`) is zero gives the hcf

```py
def hcf(a, b):
    while(b):
        a, b = b, a % b
    return a
```

```py
hcf(21, 49) # 7
```
