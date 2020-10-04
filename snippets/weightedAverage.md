---
title: weightedAverage
tags: math,beginner
---

Returns the weighted average of two or more numbers.

```py
def weightedAverage(X,W) : 
    sum = 0
    numWeight = 0
    i = 0
    while  i < len(A) : 
        numWeight = numWeight + A[i] * W[i] 
        sum = sum + W[i] 
        i = i + 1
    return (float)(numWeight / sum) 
```

```py
weightedAverage([1, 2, 3],[1,2,2]) //2.2
```
