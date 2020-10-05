---
title: function_name
tags: utility,intermediate
---

Checks if a number is palindrome

-   Compares the number with its reverse in string type

```py
def int_palindrome(a):

  return str(a)==str(a)[::-1]
```

```py
int_palindrome(121) # True
int_palindrome(12) # False
```
