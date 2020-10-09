---
title: find_and_replace
tags: string,beginner
---

Finds occurrences of a substring in a string and replaces them with another substring.

- Use the String `replace()` method to find and replace the occurrences of the old substring with that of the new substring

```py
def find_and_replace(newSubString, oldSubString, fullString):
  return fullString.replace(newSubString, oldSubString)
```

```py
find_and_replace("p", "m", "mama") # papa
```
