---
title: merge_dictionaries2
tags: dictionary,intermediate
firstSeen: 2021-10-01T14:42:35+03:00
---

Merges two dictionaries.

- Create a new `dict` utilizing `dict.__init__`'s signature which accepts a mapping for initialization as well as key-value pairs, supplied in the form of keyword arguments.
- Please, note that the second dictionary, whose elements get supplied in the form of keyword arguments to `dict.__init__`, must contain keys of type `str` only.

```py
def merge_dictionaries(d1, d2):
  return dict(d1, **d2)
```

```py
ages_one = {
  'Peter': 10,
  'Isabel': 11,
}
ages_two = {
  'Anna': 9
}
merge_dictionaries(ages_one, ages_two)
# { 'Peter': 10, 'Isabel': 11, 'Anna': 9 }
```
