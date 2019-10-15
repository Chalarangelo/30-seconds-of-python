---
title: factorial_using_gamma
tags: math,beginner
---

Uses the `math.gamma` function (from the Python 3 `math` module) to compute the factorial of a number.
This approach is generally a bit faster than using a recursive function. 
`factorial_using_gamma` only accepts positive integers, in order to closely resemble the recursive factorial function.

```py
import math

def factorial_using_gamma_function(num):
     if not ((num>=0) and (num % 1 == 0)):
             raise Exception(
                     f"Number( {num} ) can't be floating point or negative ")
     return math.gamma(num+1)
```

```py
factorial_using_gamma_function(4) #24.0
```
