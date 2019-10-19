---
title: is_triangle
tags: math,list,beginner
---

Returns True if the given angles form a triangle or else it returns False.

Use `sum()` to sum the given angles.

```py

def is_triangle(*args):
    return sum(args) == 180
```

```py
is_triangle(*[30,60,90]) # True
is_triangle(10, 20, 30) # False
```
