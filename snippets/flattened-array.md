---
title: flattened_array
tags: numpy,beginner
---

A numpy matrix can be reshaped into a vector using reshape function with parameter -1

- This is beacuse The new shape should be compatible with the original shape.
- If an integer, then the result will be a 1-D array of that length. One shape dimension can be -1. 
- In this case, the value is inferred from the length of the array and remaining dimensions.
- The same can also be done using ravel() function of numpy.array

```py
import numpy as np
def flattened_array(nums):
  return nums.reshape(-1)
```

```py
nums=np.array([[1,3],[6,2]])
flettened_array(nums) #[1,3,6,2]
```
