---
title: web site availability checker
tags: request,beginner
---

Checks the entered website is avalable

- Use requests library.

```py
import requests

#200 is the success status code of requests there fore it checks whether 200 is there.
try:
    request = requests.get('http://www.sliit123.lk')
    if request.status_code == 200:
        print('Web site exists')
except:
    print("Website does not exists")
```
