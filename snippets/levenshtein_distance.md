---
title: levenshtein_distance
tags: string,algorithm,intermediate
firstSeen: 2021-10-07T20:34:00-04:00
---

Uses dynamic programming to calculate the difference between two strings according to the Levenshtein distance algorithm.

- If either of the two strings has a `length` of zero, return the `length` of the other one.
- Create a 2D array (list of lists) to be populated with the Levenshtein distances between each pair of prefixes of the source and target strings.
- Use a `for` loop to iterate over the letters of the target string and a nested `for` loop to iterate over the letters of the source string.
- Calculate the cost of substituting the letters corresponding to `i - 1` and `j - 1` in the target and source respectively (`0` if they are the same, `1` otherwise).
- Use `Math.min()` to populate each element in the 2D array with the minimum of:
    - The cell above incremented by one
    - The cell to the left incremented by one
    - The cell to the top left incremented by the previously calculated cost.
- Return the last element of the last row of the produced array.

```py
def levenshteinDistance(s, t):
    m = len(s)
    n = len(t)
    if m == 0 return n
    if n == 0 return m
    dists = [[i] for i in range(1, m + 1)]
    dists.insert(0, list(range(0, n + 1)))
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            cost = 0
            if s[i - 1] != t[j - 1]:
                cost = 1
            dists[i].insert(j, min(dists[i - 1][j] + 1,
                               dists[i][j - 1] + 1,
                               dists[i - 1][j - 1] + cost))
    return d[-1][-1]
```

```py
levenshtein('duck','dark') # 2
```
