---
title: sample
tags: list,random,beginner
---

Returns a random element from a list.

Use `random.choice()` to select at random an element from a list.



```py
from random import choice

def sample(items):
  return choice(items)
```

```py
sample([3, 7, 9, 11]) # 9
```
