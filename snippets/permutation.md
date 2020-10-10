---
title: allPermutations
tags: string,beginner,permute
---

Prints all the permutations of a given string

- Use `permutations(string)` function of inbuilt itertools library in python

```py
from itertools import permutations 
  
def allPermutations(str): 
  permList = permutations(str) 
  for perm in list(permList): 
    print (''.join(perm))
```

```py
allPermutations('ABC')
# ABC
# ACB
# BAC
# BCA
# CAB
# CBA
```
