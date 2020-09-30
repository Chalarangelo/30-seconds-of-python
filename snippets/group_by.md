---
title: group_by
tags: list,dictionary,intermediate
---

Groups the elements of a list based on the given function.

- Use `fn` to map the values of the list to the keys of a dictionary.

```py
from collections import defaultdict

def group_by(lst, fn):
    d = defaultdict(list)
    for el in lst:
        d[fn(el)].append(el)
    return d
```

```py
from math import floor
group_by([6.1, 4.2, 6.3], floor) # {4: [4.2], 6: [6.1, 6.3]}
group_by(['one', 'two', 'three'], len) # {3: ['one', 'two'], 5: ['three']}
```
