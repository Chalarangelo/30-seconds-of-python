---
title: all_equal
tags: list,beginner
---

Comprueba si todos los elementos de una lista son iguales.

Use [1:] y [:-1] para comparar todos los valores en la lista dada.

```py
def all_equal(lst):
  return lst[1:] == lst[:-1]
```

```py
all_equal([1, 2, 3, 4, 5, 6]) # False
all_equal([1, 1, 1, 1]) # True
```
