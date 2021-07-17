---
title: mean_absolute_error
tags: math,intermediate
---

Absolute error refers to the magnitude of difference between the prediction of an observation and the true value of that observation. 
`MAE(Mean Absolute Error)` takes the average of absolute errors for a group of predictions and observations as a measurement of the magnitude of errors for the entire group.

Use `zip()` to hold two lists and in the for loop take the absolute difference with between these then return average.
if they are not the same length, it will return `Exception`.

```py
def mean_absolute_error(y_true, y_pred):
  dif = list()
  if len(y_true) == len(y_pred):
    zip_object = zip(y_true, y_pred)
    for yt, yp in zip_object:
      dif.append(abs(yt-yp))
    return sum(dif) / len(dif)
  else:
    raise Exception('It must be same length')
```

```py
mean_absolute_error([10, 11, 7], [11, 12, 8]) # 1.0
mean_absolute_error([5, 4], [7, 6, 5])	# It must be same length
```
