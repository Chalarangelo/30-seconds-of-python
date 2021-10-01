---
title: is_strong
tags: web,password,intermediate
firstSeen: 2021-10-01T13:10:00+05:30
---

This snippet checks if the password is strong or weak

- It take a password as an argument
- Check if the if the password has:
  - One uppercase letter
  - One lowercase letter
  - One special character
  - One number
- Required password length can be changed by changing `minimum_length` and `maximum_length` variables in the function

```py
import re
def is_strong(myPassword):
    minimum_length = 8
    maximum_lenth = 16
    pattern ="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{"+ f"{minimum_length},{maximum_lenth}" +"}$"
    return bool(re.match(pattern, myPassword))
```

```py
function_name('HelloWorld@1234') # True
```
