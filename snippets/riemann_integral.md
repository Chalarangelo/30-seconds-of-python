---
title: riemann_integral
tags: math,function,list,advanced
---

It calculates the *Riemann Integra*l using the *Trapezoidal Rule*. The Riemann Integral calculates the area under 
the curve of a given function `f` over the interval `[a, b]` on the x-axis. It does that by dividing the
interval `[a, b]` in `n > 0` equal sub-intervals.

- Define the width of each trapezoid `w`.
- Use `range()`, list comprehension and `sum()` to sum the heights of the trapezoids.
- Multiply the sum of heights with the width.

```py
def riemann_integral(f, a, b, n):
  w = (b - a)/n
  riemann_sum = 0.5*f(a) + sum([f(a + i*w) for i in range(1, n)]) + 0.5*f(b)
  riemann_sum *= w
  return riemann_sum
```

```py
riemann_integral(lambda x: 4.0/(1 + x**2), 0, 1, 250) # approximation of pi=3.14
```
