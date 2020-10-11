---
title: switch_case
tags: dictionary,intermediate
---

The replacement of Switch Case in Python.

- Unlike other programming languages, Python doesn't have a `switch` or `case` statement, for an alternative, we can use dictionary mapping.
- Create a dictionary of desired outcomes, you can even substitute functions instead of the regular data i.e. string, int.
- Call the dictionary mapping using the `get` method, pass the first parameter as the desired key and second parameter as fall-back value.
- In the example, if `switch_case` mapping won't find a particular match, it returns `None` otherwise returns the respective value. 

```py
def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def switch_case(case, n1, n2):
  operation_mapping = {
    '+': add,
    '-': subtract,
  }

  target_func = operation_mapping.get(case, None)
  return target_func(n1, n2) if target_func else 'No match found!'
```

```py
switch_case('+', 1, 2) # 3
switch_case('*', 1, 2) # No match found!
```