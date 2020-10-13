---
title: geometric_mean
tags: math,average,intermediate
---

Returns the average of two or more numbers using the geometric mean.

- A function that returns the product of all of the `*args` provided, to the root of `len(args)`.

```py
def average(*args):
  total = 1
  
  for num in args:
    total = total * num
    
  mean = total ** (1.0/len(args))
  return mean
```

```py
average(*[2, 3, 4]) # 2.8844991406
average(2, 3, 4) # 2.8844991406
```
