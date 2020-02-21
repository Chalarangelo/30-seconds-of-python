---
title: average_by
tags: matematicas,lista,funcion,intermedio
---


Devuelve el promedio de una lista, después de asignar cada elemento a un valor utilizando la función proporcionada.

Use `map ()` para asignar cada elemento al valor devuelto por `fn`.
Use `sum ()` para sumar todos los valores mapeados, dividirlos por `len (lst)`.

```py
def average_by(lst, fn=lambda x: x):
  return sum(map(fn, lst), 0.0) / len(lst)
```

```py
average_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda x: x['n']) # 5.0
```
