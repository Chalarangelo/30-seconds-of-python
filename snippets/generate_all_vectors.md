---
title: generate_all_vectors
tags: list,intermediate,recursion,math
firstSeen: 2021-07-21T16:25:00+01:00
---

Generate all possible distinct n-dimension vectors from a given array of elements.

- Basic case is when vector dimension (dim) is 1. Return the array of basis.
- To build a vector with dim n, loop over vectors of dim n - 1 and append to them basis from the array of basis.

```py
def generate_all_vectors(arr_basis, vec_dim):
  if vec_dim == 1:
    return [[basis] for basis in arr_basis]

  return [[*vec, basis] for basis in arr_basis for vec in generate_all_vectors(arr_basis, vec_dim - 1)]
```

```py
generate_all_vectors(arr_basis=[0, 1], vec_dim=1) # [[0], [1]]
generate_all_vectors(arr_basis=[0, 1], vec_dim=2) # [[0, 0], [1, 0], [0, 1], [1, 1]]
```
