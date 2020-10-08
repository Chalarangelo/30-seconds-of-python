---
title: dict_to_defaultdict
tags: utility,intermediate,dictionary
---

Converts a dictionary to a [defaultdict](https://docs.python.org/3.8/library/collections.html#collections.defaultdict)

- dict_to_defaultdict takes in a dictionary (called original_dict) and a valid [Callable](https://stackoverflow.com/questions/111234/what-is-a-callable) (called default)
- result is the defaultdict that is built from the original dict

```py
def dict_to_defaultdict(original_dict, default):
  from collections import defaultdict
  result = defaultdict(default)
  for key in original_dict:
    result[key] = original_dict[key]
  return result
```


```py
user = {'Name':'John',
'Age':13}

user = dict_to_defaultdict(user, lambda:False) # defaultdict(<function <lambda> at 0x000002CF4C278E50>, {'Name': 'John', 'Age': 13})
user['Non existant Key'] # Returns False
```