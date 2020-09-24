---
title: merge
tags: list,math,advanced
---

Merges two or more lists into a list of lists, combining elements from each of the input lists based on their positions.

- Use `max` combined with list comprehension to get the length of the longest list in the arguments.
- Use `range()` in combination with the `max_length` variable to loop as many times as there are elements in the longest list.
- If a list is shorter than `max_length`, use `fillvalue` for the remaining items (defaults to `None`).
- [`zip()`](https://docs.python.org/3/library/functions.html#zip) and [`itertools.zip_longest()`](https://docs.python.org/3/library/itertools.html#itertools.zip_longest) provide similar functionality to this snippet.

```py
def merge(*iterables, fillvalue=None):
  max_length = len(max(iterables, key=len))
  for i in range(max_length):
    yield [dict(enumerate(ele)).get(i, fillvalue) for ele in iterables]
```

```py
merges = list(merge('ABCD', 'xy', fillvalue='NA'))
print(merges) # [['A', 'x'], ['B', 'y'], ['C', '-'], ['D', '-']]

merge1 = list(merge(['a', 'b'], [1, 2], [True, False]))
print(merge1) # [['a', 1, True], ['b', 2, False]]

merge2 = list(merge(['a'], [1, 2], [True, False])) 
print(merge2) # [['a', 1, True], [None, 2, False]]))

merge3 = list(merge(['a'], [1, 2], [True, False], fillvalue = '_'))
print(merge3) # [['a', 1, True], ['_', 2, False]]))
```
