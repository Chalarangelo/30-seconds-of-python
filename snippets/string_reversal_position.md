---
title: string_reversal_position
tags: String,reversal,intermediate
---
Reverses a given string from the `ith position`

If `i=0` the entire string gets reversed. By default `i=0`

```py
def string_reversal_position(string,i=0):
  return string[:i] + string[i:][::-1]
```

```py
string_reversal_position("hello") # olleh
string_reversal_position("hello",1) # holle
```
