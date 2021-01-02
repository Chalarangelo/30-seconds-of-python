---
title: gcd_of_two
tags: for, range,intermediate
---

Find the GCD of Two numbers

- Find the minimum number by using `min()`
- Iterate from 1 to minimum of two
- If both the numbers divided by the number in the range`(1 to minOfTwo)`
- Then update gcd value
- Finally return the GCD value

```py
def gcd_of_two(a,b):
    for i in range(1, min(a,b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd
```

```py
gcd_of_two(12, 42) # 6
```
