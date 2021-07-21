---
title: integrate
tags: list,intermediate,math
firstSeen: 2021-07-21T16:31:00+01:00
---

Compute the intergral of a function (defined by x-y arrays) using the trapezoidal rule.

- In each iteration of the loop, compute the area of the trapezoid defined by `(x[i], y[i], y[i+1], x[i+1])`
- Add this area to the sum of the areas of the previous trapezoids
- This funtion assume that length of x and y is greater than 1 and that the elements of x array are in a increasing order (`x[i] < x[i+1]`)

```py
def integrate(x, y):
  sum_trapezoids, n = 0, len(x)

  for i in range(n-1):
    sum_trapezoids += (y[i+1] + y[i]) * (x[i+1] - x[i]) / 2 

  return sum_trapezoids
```

```py
x = [i * 0.01 for i in range(100 + 1)]
y = [t ** 2 for t in x]

integrate(x, y) # 0.33335000000000004
```
