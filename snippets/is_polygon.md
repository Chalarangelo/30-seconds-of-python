---
title: is_polygon
tags: math,beginner
firstSeen: 2021-08-08T12:49:27+05:30
---

Takes list of possible sidelengths and determines whether a two-dimensional polygon with such sidelengths can exist. 

- Use `list.sort()` to arrange sidelengths in ascending order.
- Use `list.pop()` to remove the largest sidelength form the list and to obtain it for comparison.
- Use `sum(list)` to add rest of the sidelengths.
- Return a boolean value for the `<` comparison of the largest sidelength with sum of the rest.

```py
def is_polygon(in_list):
  in_list.sort()
  return in_list.pop() < sum(in_list)
```

```py
is_polygon([6, 10, 5]) # True
is_polygon([3, 7, 13, 2]) # False
```
