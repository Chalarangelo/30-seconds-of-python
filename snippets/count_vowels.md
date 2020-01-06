---
title:  countVowels
tags: string,beginner
---

Returns number of vowels in the provided string.

The `casefold()` method returns a string where all the characters are lower case.

```py
def count_vowels(ip):
    ip = ip.casefold()
    return {x:sum([1 for char in ip if char == x]) for x in 'aeiou'}
```

```py
count_vowels("hello World!") # {'a': 0, 'u': 0, 'o': 2, 'e': 1, 'i': 0}   
```
