---
title: map_dictionary
tags: list,dictionary,intermediate
firstSeen: 2020-04-07T19:53:48+03:00
lastUpdated: 2021-10-26T12:28:27Z
---

Maps the values of a list to a dictionary using a function, where the key-value pairs consist of the original value as the key and the result of the function as the value.

- Use dictionary comprehension to apply the function `fn` to all elements of the list and generate a dictionary.

```py
def map_dictionary(itr, fn):
  return {x:fn(x) for x in itr}
```

```py
map_dictionary([1, 2, 3], lambda x: x * x) # { 1: 1, 2: 4, 3: 9 }
```
