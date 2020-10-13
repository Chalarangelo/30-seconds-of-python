---
title: roughly_equal
tags: utility,math,beginner
---

Checks if two numbers are roughly equal to each other.

- Uses `abs(x)` to handle problems with plus/minus sign
- Epsilon is used to determine an uncertainty-range.

```py
def roughly_equal(a, b, epsilon=0.01):
    return abs(a-b) < epsilon
```

```py
import math
roughly_equal(math.pi, 3.14) # True
```
