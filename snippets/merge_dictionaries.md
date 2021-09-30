---
title: merge_dictionaries
tags: dictionary,intermediate
firstSeen: 2020-04-16T19:28:35+03:00
lastUpdated: 2020-11-02T19:28:27+02:00
---

Merges two or more dictionaries.

- `ChainMap` groups multiple dicts together to create a single, updateable view. Casting the returned view to `dict` will return the merged dictionary. NOTE: the `reversed` os used to respect the order of the gived input dictionaries.

```py
from collections import ChainMap

def merge_dictionaries(*dicts):
    return dict(ChainMap(*reversed([*dicts])))
```

```py
ages_one = {
  'Peter': 10,
  'Isabel': 11,
}
ages_two = {
  'Anna': 9
}
merge_dictionaries(ages_one, ages_two)
# { 'Peter': 10, 'Isabel': 11, 'Anna': 9 }
```
