---
title: current_datetime
tags: date,beginner
---

Get the current date and time

- Use `now()` function to get the current date and time.
- Use `strftime` function to format the output in the format 'Year-Month-Date Hour:Minute:Second'

```py
from datetime import datetime

def current_datetime():
  today = datetime.now()
  return today.strftime("%Y-%m-%d %H:%M:%S")
```

```py
current_datetime() # 2020-10-04 15:20:21
```
