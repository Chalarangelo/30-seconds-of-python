---
title: is_json
tags: json
---

Checks if a given string is valid JSON.

- Use `json.loads()` to attempt to load the string as a JSON object

```py
import json

def is_json(jsn):
  try:
    json_object = json.loads(jsn)
  except ValueError as e:
    return False
  return True
```

```py
is_json('{ "id":69}') # True
is_json("{ 'id':69}") # False
```
