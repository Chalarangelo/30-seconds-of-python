---
title: get_keys_dict
tags: list, dictionary, intermediate
---

Returns the list of keys in dictionary filtered based on the values list.

```py
def get_keys_dict(my_dict: dict, search_values: list) -> list:
    return [
        key
        for key, value in filter(lambda item: item[1] in search_values, my_dict.items())
    ]

```

```py
my_dict = {'C' : 0, 'C++' : 1, 'Java' : 2, 'Python' : 3}
search_values = [1, 3]
result = get_keys_dict(my_dict=my_dict, search_values=search_values)
print(result) #  Output  ['C++', 'Python']
```
