---
title: standard_deviation
tags: math,statistics,beginner
firstSeen: 2021-10-01T06:43:12+0000
---

Finds the standard deviation of list of numbers.

- The deviation function takes one argument (list = list of elements).
- Uses this [Formula](https://www.mathsisfun.com/data/standard-deviation-formulas.html) to calculate SD.

```py
def deviation(list):
    mean = sum(list)/len(list) #calculates mean
    minus = [x - mean for (x, mean) in zip(list, [mean]*len(list))] #element wise substraction with mean

    return  (sum([i**2 for i in minus])/len(list))**(0.5) 

```

```py
foo = [1,2,3,4,5]
deviation(foo) # 1.41421
```
