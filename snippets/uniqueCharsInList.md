---
title: uniqueCharsInList
tags: utility,beginner
---

Returns all unique chars in list of strings.

- input accepts list of chars and strings.
- Result is unordered list.

```py
def uniqueCharsInList(list):
  return [c for c in ''.join(set(''.join(list)))]
```

```py
uniqueCharsInList(['testing', 'aaaa']) # ['t', 'g', 's', 'n', 'a', 'i', 'e']
uniqueCharsInList(['a', 'c', 'b']) # ['b', 'c', 'a']
```
