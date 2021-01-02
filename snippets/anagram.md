---
title: anagram
tags: Collections, Counter,intermediate
---

This method can be used to check if `two strings` are anagram or not


- An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once
- Import the `Counter` method from `collections`
- `Counter(first)` and `Counter(second)` will have the counts of the letters in a `dict` format
- If both the `dict` have same `key-value` pairs it returns True

```py
from collections import Counter

def anagram(first, second):
    return Counter(first) == Counter(second)
```

```py
anagram("listen", "silent") # True
```
