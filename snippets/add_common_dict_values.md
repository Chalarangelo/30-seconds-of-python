---
title: Combining Dictionaries By Adding Values For Common Keys
tags: dictionary, intermediate
author: highnessatharva
---

A Python function to merge multiple dictionaries and add the values for common keys present.

- Pass the dictionary items to the `add_common_dict_values ` function which utilizes defaultdict.

- Map the `items` from the dictionary  and store it in dict_items

- For every key in the orignal dictionaries, iterate through each of the values using the `chain` function of the `itertools` module.

- Finally, iterate over the newly obtained values and using the `sum` function store them in the newly created dictionary which is printed.

```py
from collections import defaultdict
from itertools import chain
from operator import methodcaller

def add_common_dict_values(*dicts):
  # initialise defaultdict of lists
  dd = defaultdict(list)

  # iterate dictionary items
  dict_items = map(methodcaller('items'), (x for x in dicts))
  for k, v in chain.from_iterable(dict_items):
    dd[k].extend(v)

  #store the sum of the values into another dictionary and print it.
  result = 0
  result_dict = {}
  for k, v in dd.items():
    for i in v:
      result = sum(v)
      result_dict[k] = result
  print(result_dict)

# dictionaries with non-equal keys, values all lists for simplicity
one = {'a': [100],  'c': [50], 'b': [200], 'e': [250]}
two = {'a': [200], 'c': [150], 'b': [400], 'd': [1000]}
three = {'a': [300], 'c': [250], 'b': [600], 'e': [250]}
# {'a': 600, 'c': 450, 'b': 1200, 'e': 500, 'd': 1000}
add_common_dict_values(one, two, three)
```
