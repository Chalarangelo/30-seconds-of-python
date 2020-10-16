---
title: ishappy
tags: math,intermediate
---

- In number theory, a Happy number is a number which eventually reaches 1 when replaced by the sum of the square of each digit.
Example:
13 is a happy number as,</br>
1<sup>2</sup> + 3<sup>2</sup> = 10 </br>
1<sup>2</sup> + 0<sup>2</sup> = 1
```py
def ishappy(n):
    visited = set()
    while n!=1 and not n in visited:
        visited.add(n)
        n = sum(map(lambda x:int(x)**2, str(n)))
    return not n in visited
```

```py
ishappy(13) #True
ishappy(19) #True
ishappy(22) #False
```
