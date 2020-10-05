---
title: slugify
tags: string,regex,intermediate
---

Converts a string to a URL-friendly slug using regex.

- At first `lower` and `strip` functions will normalize the input string.
- Regex converts spaces, dashes and underscores with `-` and remove special characters.

```py
import re

def slugify(input_str):
  input_str = input_str.lower().strip()
  input_str = re.sub(r'[^\w\s-]', '', input_str)
  input_str = re.sub(r'[\s_-]+', '-', input_str)
  input_str = re.sub(r'^-+|-+$', '', input_str)
  return input_str
```

```py
slugify('Hello World') # 'hello-world'
```
