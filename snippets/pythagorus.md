---
title: pythagorus
tags: math, pythagorus, beginner
firstSeen: 2021-07-09T03:13:33+0000
---

Function takes an argument p, b and h which is the side of right angle triangle to find the missing side and it can also
tell if the sides are of right angled triangle or not

- For example: If you want to find hypotenuse(h) of a right angled triangle with perpendicular(p) = 4 and base(b) = 3. Then, hypotenuse(h) = 5.
- The above example is saying this h = sqrt(4^2 + 3^2) or, h = 5 and if h = 5, p = 3, b = 4. Then, the function returns true

```py
import math

def pythagorus(h=0, p=0, b=0):
  if h == 0:
    return math.sqrt(p**2 + b**2)

  elif p == 0:
    return math.sqrt(h**2 - b**2)

  elif b == 0:
    return math.sqrt(h**2 - p**2)

  else:
    if h**2 == p**2 + b**2:
      return True

    else:
      return False
```

```py
pythagorus(p=4, h=5) #3
pythagorus(b=3, h=5) #4
pythagorus(p=4, b=3) #5
pythagorus(p=4, b=3, h=5) #True
pythagorus(p=4, b=5, h=3) #False
```
