---
title: is_anagram
tags: string,intermediate
---

Checks if a string is an anagram of another string (case-insensitive, ignores spaces, punctuation and special characters).

- Use `regex` to filter out non-alphanumeric characters, `lower()` to transform each character to lowercase.
- Sort both strings and check if all characters are equal
```py
import re

def is_anagram(s1, s2):
  s1 = re.sub('[\W_]+', '', s1.lower())
  s2 = re.sub('[\W_]+', '', s2.lower())
  return sorted(s1) == sorted(s2)
 ```

```py
is_anagram("#anagram", "Nag a ram!")  # True
```
