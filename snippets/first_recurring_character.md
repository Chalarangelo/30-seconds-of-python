---
title: first_recurring_character
tags: list,dictionary,intermediate
---

Returns the value of the first repeated character in a list.

- Create an empty `dictionary`.
- Scan each character of the input list.
- If the character is in the `dictionary` then return the `item`.
- else set the character equals to `True`.

```py
def first_recurring_character(list):
    table = {}
    for item in list:
        if item in table:
            return item
        else:
            table[item] = True
    return None
```

```py
print(first_recurring_character([2, 5, 1, 2, 3, 5, 1, 2, 4])) # 2
```
