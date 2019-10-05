---
title: get_third_quartile
tags: math,intermediate
---

Third quartile of a list of data elements is the median of the upper half (elements greater than the median) of the data which is sorted in increasing order. 

`median` is the median of the data after sorting it in increasing order using the `sort()` function. Same logic used to find median is also used to find the third quartile. 
```py
def get_third_quartile(data):
    if(len(data)==0):
        print("Data should not be empty")
        return
    data.sort()
    median = 0
    n = len(data)
    if(n%2)==0:
        median = (data[int(n/2)-1] + data[int(n/2)])/2
    else:
        median = data[int(n/2)]
    
    upper = [i for i in data if i > median]
    n_upper = len(upper)
    if(n_upper%2)==0:
        return (upper[int(n_upper/2)-1] + upper[int(n_upper/2)])/2
    else:
        return upper[int(n_upper/2)]   
   
```

```py
get_third_quartile([3, 7, 8, 5, 12, 14, 21, 15, 18, 14]) # 15
get_third_quartile([3, 7, 8, 5, 12, 14, 21, 13, 18]) # 16
```
