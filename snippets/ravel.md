---
title: ravel
tags: utility,list,intermediate
firstSeen: 2021-06-13T05:00:00-04:00
---

Flatten arbitrarily nested lists.
For example `[1, 2, [3, 4, [5, 6],[]], [7], 8]` becomes `[1, 2, 3, 4, 5, 6, 7, 8]`

- It uses a recursive approach.

```py
def ravel(nested_list):
    for item in nested_list:
        if isinstance(item, (list, tuple)):
            for subitem in ravel(item):
                yield subitem
        else:
            yield item
```

```py
nested_list = [1, 2, [3, 4, [5, 6],[]], [7], 8]
print(list(ravel(nested_list)))
```
