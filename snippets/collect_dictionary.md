---
title: collect_dictionary
tags: dictionary,intermediate
---

Inverts a dictionary with non-unique hashable values.

- Use `dictionary.items()` in combination with a loop to map the values of the dictionary to keys using `dictionary.setdefault()`, `list()` and `append()` to create a list for each one.

```py
def collect_dictionary(obj):
    inv_obj = {}
    for key, value in obj.items():
        if (type(value) == list):
            value = list(set(value))  # remove duplicates
            for v in value:
                inv_obj.setdefault(v, list()).append(key)
    else:
        inv_obj.setdefault(value, list()).append(key)

    return inv_obj
```

```py
sports = {
    "England": ['Cricket', 'Football'],
    "Pakistan": ['Hockey', 'Cricket'],
    "Brazil": "Football"
}
collect_dictionary(sports) # {'Cricket': ['Pakistan', 'England'], 'Football': ['Brazil', 'England'], 'Hockey': ['Pakistan']}
```
