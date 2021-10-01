---
title: anagrams
tags: string,counter,intermediate
firstSeen: 2020-10-01T17:33:07+03:00
---

Determine if two strings are anagrams.

- Bring the strings to a common, bag-of-characters representation, and perform a comparison with respect to that representation.

```py
from collections import Counter

def are_anagrams(str1, str2):
  return set(Counter(str1).items()) == set(Counter(str2).items())
```

```py
are_anagrams('abba', 'abab')
# True
are_anagrams('apples', 'oranges')
# False
```
