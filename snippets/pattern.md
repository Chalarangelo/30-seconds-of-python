---
title: pattern
tags: pattern,beginner
---

Print pattens in a right-angled triangle.

- Takes the unit block and rows as argument.
- using `join` method, function prints the unit blocks in the rows.

```py
def pattern(rows, unit):
    print('\n'.join(unit * i for i in range(1, rows + 1)))
```

```py
pattern(5, '*') 

# *
# **
# ***
# ****
# *****
```
