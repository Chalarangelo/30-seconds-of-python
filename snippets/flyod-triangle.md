---
title: flyod_triangle
tags: Pattern,Beginner
firstSeen: 2021-07-17T06:46:38+00:00
---

Explain briefly what the snippet does.

- This Functions create a right angled triangle pattern of consecutive natural numbers.
- This pattern starts with 1 on top left corner and consecutive fill till defined rows.

```py
def flyod_triangle(n):
    a=0
    for i in range(1,n+1,1):
        for j in range(0,i,1):
            a = a+1
            print(a,end=' ')
        print('') 
```

```py
flyod_triangle(3)
# result
# 1 
# 2 3 
# 4 5 6 
```
