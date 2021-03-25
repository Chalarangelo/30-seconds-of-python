---
title: dict_switch
tags: dictionary,intermediate
---

Use dictionary as a switch case.

- Define a unassigned dictionary.
- Use the built-in method `get` as a `switch`.
- Use the default argument of `get` for a default value if the key is not found.
- Pass in any argument with `()` at the end if necessary.

```py
def dict_switch(case, value):
  return {
      "ten_times_of": lambda x: 10*x,
      "twenty_times_of": lambda x: 20*x,
      "thirty_times_of": lambda x: 30*x,
  }.get(case, "thirty_times_of")(value)
```

```py
dict_switch("ten_times_of", 5) # 50
```
