---
title: average
tags: matematicas,listas,principiante
---


Devuelve el promedio de dos o más números.

Use `sum ()` para sumar todos los `args` proporcionados, divida por` len (args) `.

```py
def average(*args):
  return sum(args, 0.0) / len(args)
```

```py
average(*[1, 2, 3]) # 2.0
average(1, 2, 3) # 2.0
```
