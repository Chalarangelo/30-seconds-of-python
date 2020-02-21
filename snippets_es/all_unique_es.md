---
title: all_unique
tags: listas,principiante
---

Retorna `True` si todos los valores en una lista son únicos, `False` de lo contrario.

Usa `set()` en la lista dada para eliminar duplicados, use `len ()` para comparar su longitud con la longitud de la lista.

```py
def all_unique(lst):
  return len(lst) == len(set(lst))
```

```py
x = [1, 2, 3, 4, 5, 6]
y = [1, 2, 2, 3, 4, 5]
all_unique(x) # True
all_unique(y) # False
```
