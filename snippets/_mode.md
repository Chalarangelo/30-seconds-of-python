---
title: _mode
tags: math,list,beginner
---

Returns the mode of two or more numbers.

Use inbuilt statistics.mode() to calculate the mode.

```py
import statistics
def _mode(*args):
    return statistics.mode(args)
```

```py
_mode(*[1, 2, 3, 3]) # 3
_mode(1, 2, 3, 3) # 3
```
