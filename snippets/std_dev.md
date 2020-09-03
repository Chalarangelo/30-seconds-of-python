---
title: std_dev
tags: math,list,function,intermediate
---

Calculates standard deviation of a list.

Used `sum` and `len` to calculate `mean` . Used for loop to calculate standard deviation .

```py
def std_dev(data):
  mean = 1.0 * sum(data) / len(data)
  sigma = 0
  for d in data:
  	sigma += (d - mean) ** 2
  sigma = (sigma / len(data)) ** 0.5

  return sigma
```

```py

std_dev([7, 12, 23, 24, 16]) # 6.468384651518491
std_dev([10, 12, 23, 23, 16, 23, 21, 16]) # 4.898979485566356

```
