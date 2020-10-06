---
title: max_lists
tags: list,function,max
---

Returns the largest value in the given lists

```py

def maxlists(*lists):
    out = []
    for l in lists: out += [i for i in l]
    return max(out)
  
```

```py
maxlists(
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
) # 9
```
