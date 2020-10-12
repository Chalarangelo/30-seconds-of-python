---
title: reverse_dict
tags: dictionary,intermediate
---

Reverses the keys and values in a dictionary.

- Uses dictionary comprehension to reverse the items from the list of tuples from `original_dict.items()`.

```py
def reverse_dict(original_dict):
  reversed_dict = {value:key for (key, value) in original_dict.items()}
  return reversed_dict
```

```py
original_dict = {1:'a', 2:'b', 3:'c'}
print(reverse_dict(original_dict)) # {'a':1, 'b':2, 'c':3}
```
