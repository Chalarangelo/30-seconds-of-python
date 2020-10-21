---
title: int_to_any_base
tags: utility,intermediate
---

Convert an integer to any base up to base 36 (0-10 + A-Z). 

- Iteratively divides a number by the base size
- On each iteration reduce the current value and update the converted string
- stop dividing when the integer has been reduced
- lastly revert the string or empty string `"0"` if invalid numbers are passed

```py
def int_to_any_base(s, b):
    BS="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while s:
        res+=BS[s%b]
        s//= b
    return res[::-1] or "0"
```

```py
int_to_any_base(12345, 2) # 11000000111001
```
