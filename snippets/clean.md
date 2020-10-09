---
title: find
tags: string,beginner
---

Returns clean string without ascii chars and extra spaces.

- Use list comprehension and `next()` to return the first element in `lst` for which `fn` returns `True`.

```py
import re
from unidecode import unidecode
def clean(s):
  s = re.sub(r'\s+','',s)
  s = s.strip()
  return unidecode(s)
```

```py
clean(' How is the    weather today?') # 'How is the weather today?'
clean('Hello   World µ¶ Ôxygen') # 'Hello World uP Oxygen'
```
