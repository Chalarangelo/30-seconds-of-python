---
title: curry
tags: function,intermediate
---

Curries a function.

- Use `functools.partial()` to return a new partial object which behaves like `fn` with the given arguments, `args`, partially applied.

```py
from functools import partial

def curry(fn, *args, **kvargs):
  return partial(fn, *args, **kvargs)
```

```py
def add(x, y): return x + y
add10 = curry(add, 10)
add10(20) # 30
```
