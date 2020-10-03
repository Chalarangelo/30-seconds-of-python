---
title: is_leap_year
tags: math,beginner
---

The function checks if the given year is leap year or not.

- Use the modulo operator (`%`) to check if the year is divisible by 4, 100, 400.

The conditions are:
- If year is divisible by 4 and not divisible by 100 then **True** like 2016, 2020
- else if year is divisible by 100 and divisible by 400 then **True** like 1600, 2000
- else **False** like 1800, 2010, 2019

```py
def is_leap_year(year):
  return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
```

```py
is_leap_year(2000) # True
is_leap_year(1900) # False
is_leap_year(2020) # True
is_leap_year(2100) # False
```
