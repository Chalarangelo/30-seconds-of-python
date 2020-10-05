---
title: anagrams
tags: utility,beginner
---

Explain briefly what the snippet does.

- Input of 2 strings
- Uses counter to check how many times each charater occurs
- If the number of characters and their frequencies match, they are anagrams

```py
from collections import Counter
def anagrams(first, second):
  return Counter(first) == Counter(second)
```

```py
anagram("abcd3", "3acdb") # True
anagram("abed3", "3acdb") # False
```
