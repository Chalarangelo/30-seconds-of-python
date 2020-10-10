---
title: read_json
tags: json,beginner
---

Read a json file as a dictionary.

- Use the json module to load json file as a dictionary.

```py
def read_json(path_to_file):
  import json 
  with open(path_to_file, 'r') as f:
    return json.load(f)
```

```py
read_json(path) #a dictionary
```
