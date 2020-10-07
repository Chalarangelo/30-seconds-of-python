---
title: function_name
tags: utility,intermediate
---

Returns the name of a function as a string.

- Only gets the object property `__name__`.

```py
def function_name(fn):
  return fn.__name__
```

```py
function_name(print) # print
```
