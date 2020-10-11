---
title: symmetric_difference_by
tags: list,function,intermediate
---

Returns the symmetric difference between two lists, after applying the provided function to each list element of both.

- Create a `set` by applying `fn` to each element in every list, then use the symmetric difference operator of sets.

```py
def symmetric_difference_by(a, b, fn):
  return list(set(map(fn, a)) ^ set(map(fn, b)))
```

```py
from math import floor
symmetric_difference_by([2.1, 1.2], [2.3, 3.4],floor) # [1.2, 3.4]
```