---
title: is_anagram
tags: string,intermediate
---

Checks if a string is an anagram of another string (case-insensitive, ignores spaces, punctuation and special characters).

Use `s.replace()` to remove spaces from both strings.
Use python's inbuilt Counter class from collections package and comapare the both the objects.

Counter class returns its own instance which consists of the element and its respective occurance count in the iterable
Eg:
```py
>>Counter("anagram")
Counter({'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1})
```

```py
from collections import Counter
def is_anagram(s1, s2):
  _str1, _str2 = s1.replace(" ", ""), s2.replace(" ", "")
  return Counter(_str1.lower()) == Counter(_str2.lower()) #compare both Counter objects
```

```py
is_anagram("anagram", "Nag a ram")  # True
```
