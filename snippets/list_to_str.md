---
title: stringify_list
tags: utility,beginner
firstSeen: 2021-08-03T023:27:00-04:00
---

The stringify_list function takes the contents of a list and
returns a string of the list contents optionaly separated by a provided separator.

- Sets `out_str` to an empty string
- Loops over all ov the items in the provided list
- Append the current list item to `out_str` + the provided seperator if any
- If the current list item is the last item in the list, append it to `out_str` but do not append separator

```py
def stringify_list(lst, separator="") -> str:
out_str = ""
for i in range(len(lst)):
  item = lst[i]
  if i == len(lst) - 1:
    out_str += str(item)
  else:
    out_str += str(item) + separator
  return out_str
```

```py
stringify_list(["1", "2", "3"]) # result -> "123"
stringify_list(["a", "b", "c"], separator=", ") # result -> "a, b, c"
```
