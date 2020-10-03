---
title: Custom string representation for objects
tags: utility,advanced
---

Python uses a "magic methods" convention to define object interface.
For example, whenever an object is converted to string, its `__str__()` method is called.
Thus, `str(x)` is really `x.__str__()`.

- You can give your objects a custom string representation if you define a `__str__()` method.
- It's only one of the standard "magic methods", there are many more.

Example: a class for complex numbers.

```py
class MyComplex(object):
  def __init__(self, real, imaginary):
    self.real = real
    self.imaginary = imaginary

  def __str__(self):
    return "{0} + {1}i".format(self.real, self.imaginary)
```

```py
x = MyComplex(1, 2)
print(x) # 1 + 2i
```
