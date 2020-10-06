---
title: sum_lists
tags: list,function,sum
---

Creates a list in which all the given lists are extracted.

```py

def sum_lists(*lists):
    out = []
    for l in lists: out += [i for i in l]
    return out
  
```

```py
sum_lists(
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
)
'[1, 2, 3, 4, 5, 6, 7, 8, 9]'
```
