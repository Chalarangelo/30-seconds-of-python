---
title: is_within_distance
tags: math, beginner
---

Checks whether two given points are within the given Euclidian distance from each other.

- Calculates the squared Euclidian distance between the two given points, then compares it to the squared given distance.

```py
def is_within_distance(x0, y0, x1, y1, distance):
  return (x0 - x1) ** 2 + (y0 - y1) ** 2 <= distance ** 2
```

```py
is_within_distance(0, 0, 2, 2, 3) # True
is_within_distance(0, 0, 1, 1, 1) # false
is_within_distance(-5, 0, 0, 7, 8) # false
```
