---
title: unique_chars_in_list
tags: utility,beginner
---

Returns all unique chars in list of strings.

- input accepts list of chars and strings.
- Result is unordered list.

```py
def unique_chars_in_list(list):
  return [c for c in ''.join(set(''.join(list)))]
```

```py
unique_chars_in_list(['testing', 'aaaa']) # ['t', 'g', 's', 'n', 'a', 'i', 'e']
unique_chars_in_list(['a', 'c', 'b']) # ['b', 'c', 'a']
```
