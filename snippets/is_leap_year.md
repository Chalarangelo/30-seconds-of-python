---
title: is_leap_year
tags: utility,beginner
---

Checks if the provided year is a leap year. 

- Return `True` if the given `year` is a leap year, returns `False` if not. 
- Uses modulo (`%`) to check if the year is divisible by 400 and not by 100, or if the century is divisible by 400. 

```py
def is_leap_year(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return True
  return False
```

```py
is_leap_year(2020) # True
is_leap_year(2021) # False
```
