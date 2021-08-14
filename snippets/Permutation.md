---
title: Permutations
tags: math,list,permutation,recursion
firstSeen: 2021-08-14T08:30:39+05:30
---

Explain briefly what the snippet does.
- Uses `recursion`
- Extracts all elements,places them at the first position and then recursively calls the function for other elements.
- The function takes Parameter as `list`.
- Returns a `nested list`.

```py
def Permutation(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [arr]
    l = []
    for i in range(len(arr)):
        m = arr[i]
        remArr = arr[:i] + arr[i+1:]

        for p in Permutation(remArr):
            l.append([m] + p)
    return l
```

```py
Permutation([1,2,3]) # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```
