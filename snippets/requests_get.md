---
title: requests_get
tags: requests,get,beginner
---

Make a get request to a web page, and return the status code and page content

- Function takes page url and other optional arguments(parameters and timeout).
- It uses the `requests` module to issue a get request on the url.

```py
import requests

def requests_get(url, params=None, timeout=None):
  page = requests.get(url=url, params=params, timeout=timeout)
  return page.status_code, page.content
```

```py
requests_get("https://www.30secondsofcode.org/python/s/weighted-average") # (status_code, page_content)
```
