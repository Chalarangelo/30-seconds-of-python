---
title: wrap_function
tags: object-oriented-programming,intermediate
firstSeen: 2021-09-30T22:38:06+0530
---

Wraps a function to separate configuration arguments from variable arguments. Enables repeated use of the same function with same arguments without any external library like `functools`.


```py
def Adder(to_add=0):
  def apply(x):
    return x + to_add
  return apply
```

```py
add_4 = Adder(to_add=4)

add_4(2) # 6

add_4(5) # 9

#Alternate usage

Adder(to_add=10)(20) #30
```
