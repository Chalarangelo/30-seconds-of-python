---
title: Combining Dictionaries By Adding Values For Common Keys
tags: dictionary, intermediate
author: highnessatharva
---

A Python function to merge two dicitonaries and add the values for common keys present in original dictionary. 

- Firstly, define a function taking two dicitionaries as arguments and initialize `counter` as a copy of the first dictionary.
- Iterating over the keys of dicitonary 2, if the same key is present in dictonary 1 increment the value in dictionary 1 with that of the value in dicitonary 2. `dict[key]` retrieves the values.
- Finally, print the newly created dictionary with added values of overlapping dictionary keys.

```py
def combineWithValues(d1, d2):
    counter = {}
    counter = d1.copy()
    for key in d2:
        if key in counter:
            counter[key] += d2[key]
        else:
            counter[key] = d2[key]
    print(counter)
```

```py
d1 = {'a': 100, 'b': 200, 'c': 400}
d2 = {'a': 300, 'b': 200, 'd': 400}
combineWithValues(d1,d2) # {'a': 400, 'b': 400, 'c': 400, 'd': 400}
```
