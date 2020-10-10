---
title: iterate_dict
tags: dictionary,beginner
---

Iterate through a dictionary.

- Use `dictionary.items()` to return a list of tuples.
- These tuples are in format `(key,value)`.
- We can use a `for` loop to iterate through this returned `list`.

```py
def return_list(dictonary):
  return dictonary.items()
```

```py
example_dict = {'Seoul':'South Korea', 'Tokyo':'Japan'} 
for city, country in return_list(example_dict):
  pass
# [('Seoul', 'South Korea'), ('Tokyo', 'Japan')]

```
