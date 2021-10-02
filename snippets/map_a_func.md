---
title: Map a fuction
tags: General,Intermediate
firstSeen: 2021-10-02T21:53:33+03:00
lastUpdated: 2021-10-02T21:53:33+03:00
---

Given a list of numbers and a fucntion as arguements, the list is transformed my mapping it into the function.

- Let `func` be any other transformation function then we can call it as follows

```py
def map_a_func(array, func):
  return list(map(func,array))
```

```py
def square(x):
  return x**2
a=[1,2,3,4]
a=map_a_func(a,square)#[1,4,9,16]
```
