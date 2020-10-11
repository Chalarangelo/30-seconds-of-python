---
title: atleast
tags: list,function,intermediate
---

Returns `True` if the provided function returns `True` for atleast k elements in the list, `False` otherwise.

- Use `all()` in combination with `map` and `fn` to check if `fn` returns `True` for all elements in the list.

```py
def atleast(lst, k, fn=lambda x: x):
  return len(list(filter(fn, lst))) >= k
```

```py
atleast([1, 2, 3], 2, lambda x: x > 2) # False
atleast([1, 2, 3], 2) # True
```
