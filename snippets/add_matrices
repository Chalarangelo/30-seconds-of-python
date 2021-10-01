---
title: add_matrices
tags: utility,math
firstSeen: 2021-06-13T05:00:00-04:00
---

Add elements of two matrices of equal size. 

```py
def add_matrices(matrix_A, matrix_B):
  if len(matrix_A) != len(matrix_B) or len(matrix_A[0]) != len(matrix_B[0]):
    print("Please make sure the matrices are equal in size")
    return 0
    
  matrix_R = matrix_A
  for i in range(len(matrix_A)):
    for j in range(len(matrix_A[0])):
      matrix_R[i][j] = matrix_A[i][j] + matrix_B[i][j]
  return matrix_R
```

```py
X = [[2, 3, 4], [1, 5, 7], [9, 3, 2], [1, 2, 4]]
Y = [[9, 0, 11], [3, 4, 1], [1, 8, 3], [9, 3, 9]]
add_matrices(X, Y) # [[11, 3, 15], [4, 9, 8], [10, 11, 5], [10, 5, 13]]
```
