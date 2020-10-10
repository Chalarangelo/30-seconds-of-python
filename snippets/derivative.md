---
title: derivative
tags: math,function,beginner
---

Approximates the derivative of the function `f` in the point `a` using *centered differencing* formula.
For a small number `h > 0`:

- Calculate the difference between `f(a + h)` and `f(a - h)`.
- Divide the difference with `2*h`.
- If `h` is not provided, it is set to `0.01` by default.

```py
def derivative(f, a, h=0.01):
  return (f(a + h) - f(a - h))/(2*h)
```

```py
derivative(lambda x: x**2, 3, 1e-6) # derivative of x^2 is 2*x, thus 2*3 approx. 6
derivative(lambda x: x**x, 2, 1e-6) # derivative of x*x is x^x(ln(x) + 1), thus approx. 6.772
```
