---
title: first_recurring_character
tags: list,dictionary,intermediate
---

Returns the value of the first recurring character in a list.

- Explain briefly how the snippet works.
- Use bullet points for your snippet's explanation.
- Try to explain everything briefly but clearly.

```py
def first_recurring_character(array):
    table = {}
    for item in array:
        if item in table:
            return item
        else:
            table[item] = True
    return None
```

```py
print(first_recurring_character([2, 5, 1, 2, 3, 5, 1, 2, 4])) # 2
```
