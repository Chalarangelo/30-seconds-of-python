---
title: is_amstrong
tags: generator,beginner
---

Returns `True` if number is amstrong number, `False` otherwise.

Use `sum()` on the generator expression which results in individual digits raised to the power of order of given number(i.e., no of digits in given number).

```py
def is_amstrong(num):
    order = len(str(num))
    sum_of_digits = sum((int(digit)**order for digit in str(num)))
    return sum_of_digits == num 
```

```py
x = 371
y = 548
z = 1634
is_amstrong(x) # True
is_amstrong(y) # False
is_amstrong(z) # True
```
