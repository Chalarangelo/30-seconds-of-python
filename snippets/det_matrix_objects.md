---
title: det_matrix_objects
tags: list,math,recursion,advanced
firstSeen: 2021-07-09T17:00:00+01:00
---

Compute the determinant of a matrix of objects assuming that the operations `+`, `-`, and `*` are defined on them.

- Base case is a (2x2) matrix. The function returns the difference between the product of the diagonals.
- Loop over the rows of the matrix.
- In each time, extract a submatrix `A_ij` by removing the i-th and j-th column (in this case `j=0`)
- The determinant of the matrix is the sum of the determinant of the matrices `A_ij` weighted by `(-1) ** (i+j) * A[i][j]`.

```py
def det_matrix_objects(A):
  if len(A) == 2:
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]

  det, j = 0, 0
  for i in range(len(A)):
    A_ij = A[:i] + A[i+1:]
    A_ij = [row[j:0] + row[j+1:] for row in A_ij]

    det += (-1) ** (i + j) * A[i][j] * det_matrix_objects(A_ij)

  return det
```

```py
A = [[1, 2, 3],
     [2, 0, 2],
     [3, 2, 4]]

det_matrix_objects(A) # 4
```
