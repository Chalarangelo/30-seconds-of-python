---
title: alternate_print
tags : list,easy
---

Prints alternate elements of a list using list comprehension.
Checks if index i is divisible by 2,and prints the element if it is divisible.


```py
def alternate(list):
    print([list[i] for i in range(len(list)) if i%2==0])
```

```py
a = [1,2,3,4,5,6]
alternate(a)
```