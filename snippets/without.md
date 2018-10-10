### without

Function which filters out specified values from a list, returning the remaining values.

Uses built-in array functions in Python.

``` python
def without(arr, *argv):
  for value in argv:
    arr = [y for y in arr if y != value]
    
  return arr
```

``` python
without([2, 1, 2, 3], 1, 2) # [3]
```
