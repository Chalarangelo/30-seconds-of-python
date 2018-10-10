### without

Function which filters out specified values from a list, returning the remaining values.

Uses a list comprehension to rewrite the array without the filtered value.

``` python
def without(arr, *argv):
  for value in argv:
    arr = [y for y in arr if y != value]
    
  return arr
```

``` python
without([2, 1, 2, 3], 1, 2) # [3]
```
