---
title: hcf
tags: math,list,intermediate
---

Returns the highest common factor of a list of numbers.

- Applies `math.gcd` to list elements using the `functools.reduce`

```py
from functools import reduce
from math import gcd

def hcf(list):
    return reduce(gcd, list)
```

```py
hcf([88, 22, 77, 121]) # 11
```
