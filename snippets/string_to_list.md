---
title: string_to_list
tags: string,list,beginner
---

Convert a list of string representations to a list object.

- Use ast module to process trees of the Python abstract syntax grammar.
- `ast.literal_eval(node_or_string)` safely evaluate a string containing a Python literal.
- Also support tuples, dicts, sets.

```py
import ast

def string_to_list(str):
  return ast.literal_eval(str)
```

```py
lst = string_to_list('[0,1,2,[3,4],5]') # [0, 1, 2, [3, 4], 5]
type(lst) # <class 'list'>
```
