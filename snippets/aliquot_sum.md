---
title: aliquot_sum
tags: math, list, function, intermediate
---

Returns the aliquot_sum of the number.

Use `sum()` to sum all of the proper divisors of the number provided.

```py
def aliqout_sum(num):
    return sum([i for i in range(1,num) if not(num % i)])
```

```py
aliqout_sum(12) # 16
```
