---
title: max_contiguous_sum
tags:  list,function,math
---

From a list find the max sum of a continous subarray 

Store the max value in a varibale end and iteratively keep adding the array elements 
in another variable far , when far becomes lesser then 0 update far to be 0 again,
when far surpasses end update end to be equal to far and return end 

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
