---
title: two_digit_time
tags: date,beginner
firstSeen: 2021-06-28T12:15:59+0000
---

Converts hours and minutes to standard HH:MM format (adding leading zeros, if necessary).

- Takes `time` as argument and checks it against regex, if it is in expected format
- Extracts `hours` and `minutes` from `time` by `split()` function - converts it to an integer with `int()`
- Makes integer operations inside f-string to archive 2 digits on `hours` and `minutes` - returns the result

```py
def two_digit_time(time):
  if not re.compile("^([0-9]{1,2}):([0-9]{1,2})$").search(time):
    raise Exception(f"Provided time ({time}) is not supported")
  hours = int(time.split(":")[0])
  minutes = int(time.split(":")[1])
  return f"{hours:02d}:{minutes:02d}"
```

```py
two_digit_time("8:37") # "08:37"
two_digit_time("17:4") # "17:04"
two_digit_time("5:2") # "05:02"
```
