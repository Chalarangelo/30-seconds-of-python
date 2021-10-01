---
title: starmap
tags: starmap,intermediate
firstSeen: 2021-10-01T17:29:31+03:00
---

Apply a function to a collection of collections, without manually unpacking each element of the collection.

- Create a new `dict` with the same keys as a given input `dict`, and values incremented by a constant.

```py
from itertools import starmap

def add_to_values(a_dict, value): 
  return dict(
    starmap(
      lambda k, v: (k, v + value),
      a_dict.items(),
    )
  )
```

```py
apples = {
  'Peter': 10,
  'Isabel': 12,
  'Anna': 20,
}

add_to_values(apples, 5)
# {'Peter': 15, 'Isabel': 17, 'Anna': 25}
```
