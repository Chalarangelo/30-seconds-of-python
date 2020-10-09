---
title: transpose of matrix
tags: math, loops, intermediate, matrices
---

Returns list of transposed matrix rowise

```py
def transpose_matrix():
 X = [[12,7],
    [4 ,5],
    [3 ,8]]

 result = [[0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)
```

```py
transpose_matrix() 
# [12, 4, 3]
# [7, 5, 8]
```
