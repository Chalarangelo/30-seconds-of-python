---
title: swap_values
tags: tuple,beginner
firstSeen: 2020-10-02T14:24:05+03:00
---

Swap the values of two variables without explicitly declaring an auxiliary variable.

- Pack two variabes in a tuple and then unpack them in reverse order, assigning the results to the original variables.

```py
def swap(a, b):
  a, b = b, a
  return a, b

def swap2(a, b):
  return b, a
```

```py
a = 5
b = 10
a, b = swap(a, b)
# a = 10, b = 5
a, b = swap2(a, b)
# a = 5, b = 10
```
