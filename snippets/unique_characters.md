---
title: list_of_words
tags: list, intermediate
---

Returns all unique characters in a given string

Use `set()` to remove the duplicate characters, then join the unique characters into a string using `join()`.

```py
def unique_characters(string):
  unique = set(string)
  return ''.join(unique)
```

```py
my_string = "abcbcabdb"
unique_characters(my_string) # abcd
```