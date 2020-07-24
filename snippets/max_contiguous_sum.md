---
title: max_contiguous_sum
tags:  list,function,math
---

From a list find the max sum of a continous subarray

Store the max value in a varibale end and iteratively keep adding teh array elements 


```py
def max_contiguous_sum(l):
  n=len(l)
  far=0
  end=max(l)
  for i in range(n):
      far=far+l[i]
      if(far<0):
          far=0
      elif(far>end):
          end=far
  return end

```

```py
max_contiguous_sum([1, 2, 3, 4, -10]) # 10
```
