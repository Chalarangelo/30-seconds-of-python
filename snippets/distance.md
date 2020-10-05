---
title: distance
tags: math,distance
---

Returns the distance between two points.

- it takes four variables, x0, x1, y0, y1 and return the distance between x and y.

```py
from math import sqrt
def distance(x0, y0, x1, y1):
  return sqrt((x1 - x0)**2 + (y1 - y0)**2)  
```

```py
distance(1, 1, 2, 3) # 2.23606797749979
```
