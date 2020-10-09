---
title: primes_till_n
tags: list,math,intermediate
---

Generates prime number list till the number specified.

```py
from math import sqrt
def primes_till_n(limit):
  
    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2):
            return False
        return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))
  return [i for i in range(1, limit) if is_prime(i)]
```

```py
primes_till_n(10) # [2, 3, 5, 7, 9]
primes_till_n(6) # [2, 3, 5]
```
