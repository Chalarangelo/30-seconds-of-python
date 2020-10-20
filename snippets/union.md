---
title: union
tags: list,beginner
---

Returns every element that exists at least once in any of the lists.

- Create a `set` with all values of all the `lists` and convert to a `list`.

```py
def union(*lists):
  summed_lst = []
  for li in lists:
    summed_lst += li
  return list(set(summed_lst))
```

```py
union([1, 2, 2, 3], [4, 3, 2]) # [1, 2, 3, 4]
```
