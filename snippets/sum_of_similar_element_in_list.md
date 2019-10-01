---
title: sum of similar elements
tags: math,list,beginner
---

Returns the sum of similar numbers in a list.

Use `sum()` to sum all of the `count` provided.

```py
def sumx(X, n):
  return sum(X.count(n))
```

```py
sumx([1, 2, 1, 3, 1], 1) # 3.0
sumx([1, 2, 3, 2], 2) # 4.0
```
