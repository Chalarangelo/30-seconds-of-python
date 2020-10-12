---
title: default_tree
tags: utility,dictionary,intermediate
---

Create a simple tree structure without the need to explicitly initialize nested dictionaries.

- Use `defaultdict()` in the `default_tree()` function that will recursively call `default_tree()` for setting new values.

```python3
from collections import defaultdict

def default_tree():
  return defaultdict(default_tree)
```

```python3
d = default_tree()
d[0]['a'][(3, 15)] = 'leaf0'
d[0]['b']['c'] = 'leaf1'
d # {0: {'a': {(3, 15): 'leaf0'}, 'b': {'c': 'leaf1'}}}
```
