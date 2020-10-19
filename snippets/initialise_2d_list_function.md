---
title: initialise_2d_list_function
tags: utility,intermediate
---

Initializes a 2 dimensional list with values resulting from of a given function `func` of the row and column indices.

- If no function is passed then the list gets initialied with zeroes.
- Can also be used to create sample spaces (tuple elements) for events in probability.


```repoShortLang
def initialise_2d_list_function(m, n, func = lambda x,y : 0):
  return [[func(i, j) for j in range(n)] for i in range(m)]
```

```repoShortLang
initialise_2d_list_function(2, 2 ,lambda x,y : x + y) # => [[0, 1], [1, 2]]
initialise_2d_list_function(3, 3) #initializes a 3x3 matrix with zeroes
```
