---
title: to_binary_list
tags: math,list,intermediate
---

Convert all elements in an integer list to their binary notation.

- Takes a list/tuple containing integers.
- Returns a list with integers of arguement list converted to binary.

```py
def to_binary_list(lst):
  return [int(binary_string.replace("0b","")) for binary_string in list(map(bin,lst))]
```

```py
to_binary_list([1,2,3,4]) # [1, 10, 11, 100]
```
