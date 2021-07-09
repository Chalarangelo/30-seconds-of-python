---
title: natural_sum
tags: math, natural_sum, beginner
firstSeen: 2021-07-09T03:13:33+0000
---

Explain briefly what the snippet does.

- Function takes an argument n which is the number of natural numbers to calculate sum of.
- For example: if you want to calculate the sum of first 100 natural numbers then n = 100.
- The above example is saying this f(n) = 1 + 2 + 3 + 4 + 5 + ..... + n.

```py
def natural_sum(n):
  return (n * (n + 1)) / 2

```

```py
natural_sum(100) # 5050
```
