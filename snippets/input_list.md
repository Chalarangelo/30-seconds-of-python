---
title: function_name
tags: utility,intermediate
---

Accepts a list of integers from the user

-   works by using the map function on accepted input

```py
def input_list():
  a = map(int,input().split())
  return a
```

```py
# for user input 1 2 3
input_list() # [1 2 3]
```
