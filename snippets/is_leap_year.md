---
title: is_leap_year
tags: math,beginner
firstSeen: 2021-08-16T16:31:06+05:30
lastUpdated: 2021-08-16T16:31:06+05:30
---

Checks if the given year is a leap year or not.

- Use the `calendar.isleap()` method to determine if it is a leap year.
- Returns `True` if it is a leap year, `False` if it is not.

```py
import calendar

def is_leap_year(year):
  return calendar.isleap(year)
```

```py
is_leap_year(1900) # False
is_leap_year(2000) # True
is_leap_year(2001) # False
```
