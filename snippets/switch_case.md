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

switch_case = {
  '+': add,
  '-': subtract,
}
```

```py
target_func = switch_case.get('+', None)
print(target_func(1, 2) if target_func else 'No match found!') # 3
```
