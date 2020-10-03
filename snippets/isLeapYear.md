---
title: is_leap_year
tags: math,beginner
---

Checks if the given year is a leap year or not.

- Use the modulo operator (`%`) to check if year is divisible by 4, 100 and 400.

```py
def is_leap_year(year):
  return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
```

```py
is_leap_year(2000) # True
is_leap_year(1800) # False
is_leap_year(2020) # True
is_leap_year(2100) # True
```
