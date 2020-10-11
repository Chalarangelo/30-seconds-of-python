---
title: cosine_similarity
tags: math,list,intermediate
---

Takes two lists of numbers and calculates their [cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity).

- First calculates the sum of the products of corresponding values in the list.
- Uses `math.sqrt()` function to get the final denominator.
- Returns the fraction of numerator and denominator.
- Time complexity: `O(n)`.

```py
import math

def cosine_similarity(v1, v2):
  sumxx, sumxy, sumyy = 0, 0, 0
  for i in range(len(v1)):
    x = v1[i]; y = v2[i]
    sumxx += x*x
    sumyy += y*y
    sumxy += x*y
  return sumxy/math.sqrt(sumxx*sumyy)
```

```py
cosine_similarity([3, 45, 7, 2], [2, 54, 13, 15]) # 0.97228425171235
```
