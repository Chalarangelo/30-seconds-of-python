---
title: min_lists
tags: list,function,min
---

Returns the smallest value in a given list

```py

def minlists(*lists):
    out = []
    for l in lists: out += [i for i in l]
    return min(out)
  
```

```py
minlists(
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
)
'1'
```
