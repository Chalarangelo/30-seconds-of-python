### difference

Returns the difference between two arrays.

Creates sets and uses the builtin `set.difference()` [[2.7]](https://docs.python.org/2.7/library/stdtypes.html?highlight=set%20difference#frozenset.difference) / [[3.6]](https://docs.python.org/3.6/library/stdtypes.html?highlight=set%20difference#frozenset.difference) function to return the difference between `a` and `b`

```python
def difference(a, b):
    return set(a).difference(set(b))
```
``` python
difference([1, 2, 3], [1, 2, 4]) # {3}
```
