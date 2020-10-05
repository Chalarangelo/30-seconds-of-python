---
title: mod_add
tags: utility,begineer
---

Performs modular addition of 2 numbers under a given mod

-   Use modular addition property (a + b % c) % c = (a%c + b % c) % c

```py
def mod_add(a,b,c):
  ans = (a%c + b%c)%c
  return ans
```

```py
mod_add(2,6,5) # 3
mod_add(3,3,4) # 2
```
