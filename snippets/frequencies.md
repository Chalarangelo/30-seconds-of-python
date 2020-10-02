---
title: frequencies
tags: list,intermediate
---

Returns a dictionary with the unique values of a list as keys and their frequencies as the values.

- Use `list.count()` to get freq of each unique element.
- Use `dict()` constructor to return dictionary with keys as unique elements of list and their freq as values.

```py
def frequencies(lst):
  return dict((k, lst.count(k)) for k in lst)
```

```py
data = ['a', 'b', 'a', 'c', 'a', 'a', 'b']
frequencies(data) # { 'a': 4, 'b': 2, 'c': 1 }
```
