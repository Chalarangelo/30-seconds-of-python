---
title: format_seconds
tags: date,math,string,beginner
firstSeen: 2021-08-31T17:50:45+00:00
---

Returns the ISO format of the given number of seconds.

- Understand whether given seconds are negative or not by looking at their first character as a string.
- Assign the abstract value of seconds to seconds for precise calculation.
- Calculate hours with `seconds // 3600` minutes with `seconds % 3600 // 60` and seconds with `seconds % 60`.
- Use string method `zfill()` in order to ensure that all indicators consist of two digits.
- If the given seconds are negative return the indicator with a minus sign.

```py
def format_seconds(seconds: int) -> str:
  is_negative, seconds = str(seconds)[0] == "-", abs(seconds)
  if is_negative:
    return f"-{str(seconds // 3600).zfill(2)}:{str(seconds % 3600 // 60).zfill(2)}:{str(seconds % 60).zfill(2)}"
  return f"{str(seconds // 3600).zfill(2)}:{str(seconds % 3600 // 60).zfill(2)}:{str(seconds % 60).zfill(2)}"
```

```py
format_seconds(3600) # 01:00:00
format_seconds(60) # 00:01:00
format_seconds(2021) # 00:33:41
```
