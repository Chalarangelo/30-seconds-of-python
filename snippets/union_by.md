---
title: union_by
tags: list,function,intermediate
---

Returns every element that exists in any of the two lists once, after applying the provided function to each element of both.

- Create a `set` by applying `fn` to each element in `a` and `b`.
- Use the set union operator on the results above, and convert to a list.

```py
def union_by(a, b, fn):
  return list(set(map(fn, a)) + set(map(fn, b)))
```

```py
from math import floor
union_by([2.1], [1.2, 2.3], floor) # [2.1, 1.2]
```
