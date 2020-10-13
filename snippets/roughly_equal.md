---
title: roughly_equal
tags: utility,math,beginner
---

Checks if two numbers are roughly equal to each other.

- Uses `abs(x)` to handle problems with plus/minus sign
- Epsilon is used to determine an uncertainty-range. It's default value is 0.01

```py
def roughly_equal(number1, number2, epsilon=0.01):
  return abs(number1-number2) < epsilon
```

```py
import math
roughly_equal(math.pi, 3.14) # True
roughly_equal(math.pi. 3.12) # False
```
