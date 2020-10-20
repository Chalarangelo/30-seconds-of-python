---
title: chunk
tags: list,intermediate
---

Chunks a list into smaller lists of a specified size.

- Use `list()` and `range()` to create a list of the desired `size`.
- Use `map()` on the list and fill it with splices of the given list.
- Finally, return the created list.

```py
from math import ceil

def chunk(lst, size):
    chunks = []
    index = 0
    for i in range(ceil(len(lst)/size)):
            chunks.append(lst[index:index+size])
            index += size
    return chunks
```

```py
chunk([1, 2, 3, 4, 5], 2) # [[1,2],[3,4],[5]]
```
