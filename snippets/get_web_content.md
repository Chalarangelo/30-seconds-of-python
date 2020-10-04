---
title: get_web_content
tags: utility,intermediate
---

Returns the static HTML content of a webpage.

- Using `requests` and `BeautifulSoup` libraries, this snippet of code returns the static `html` of the webpage for parsing.
- The arguments accepted are: `url` (the web url) and `timeout` (timeout value of the web request in seconds)

```py
import requests
from bs4 import BeautifulSoup

def get_web_content(url,timeout):
  try:

    response = requests.get(url,timeout=timeout)

  except requests.exceptions.Timeout:
    print("Request to webpage {} timed out after {}".format(url,timeout))
  except requests.exceptions.RequestException:
    print("Request to webpage {} threw exception during request call.".format(url))

  return BeautifulSoup(response.content,features='lxml')
```

```py
get_web_content('https://www.30secondsofcode.org/python/p/1',20) # returns the html content of the web page. Timeout is 20 seconds
```
