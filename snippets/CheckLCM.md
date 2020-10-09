---
title: compute_lcm
tags: numbers,integers,beginner
---

The function takes two numbers and tell the L.C.M of the numbers

- It takes two numbers
- Then check if they evenly divides each other if not
- Then divides both with a number that evenly divides both numbers

```py
def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm
```

```py
num1 = 54
num2 = 24

print("The L.C.M. is", compute_lcm(num1, num2)) #  216
```
