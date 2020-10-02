---
title: frequencies
tags: list,intermediate
---

Returns a dictionary with the unique values of a list as keys and their frequencies as the values.

- Use a `for` loop to populate a dictionary, `f`, with the unique values in `lst` as keys, adding to existing keys every time the same value is encountered.

```py
def frequencies(lst):
  return dict((k, lst.count(k)) for k in lst)
```

```py
frequencies(['a', 'b', 'a', 'c', 'a', 'a', 'b']) # { 'a': 4, 'b': 2, 'c': 1 }
```
