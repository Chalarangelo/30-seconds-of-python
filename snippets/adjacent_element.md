---
title: adjacent_element
tags: list,beginner
firstSeen: 2021-07-15T04:25:18+00:00
---

Get adjacent elements in a list.

- Use list slice to make a copy.
- Use zip to combine two slices.
- And return with a list.

```py
def adjacent_element(li):
  return list(zip(li[:-1],li[1:]))
```

```py
li = ['a', 'b', 'c', 'd', 'e','f']
adjacent_element(li) # [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'f')]
```
