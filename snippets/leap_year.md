---
title: leap_year
tags: math,beginner
---

Checks if the given year is a leap year or not

- 'year' input is any integer
- If a year is not divisible by 4 then its not leap year
- If a year is divisible by 4 but not by 100, then its a leap year
- If a year is divisible by 4 and by 100 but not by 400, then it's not a leap year

```py
def leap_year(year):
  if (year % 4) == 0:
    if (year % 100) == 0:
      if (year % 400) == 0:
        print("{0} is a leap year".format(year))
      else:
        print("{0} is not a leap year".format(year))
    else:
      print("{0} is a leap year".format(year))
  else:
    print("{0} is not a leap year".format(year))
```

```py
leap_year(2016) #2016 is a leap year
leap_year(2010) #2010 is not a leap year
```
