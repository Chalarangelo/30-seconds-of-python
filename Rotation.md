---
title: Rotation
tags: python,list slicing
---

This is the shortest methos for doing Left or Right rotation.

- we have to pass array , n times rotation and bool value isLeft. For Left Rotation it is True and for Right it is False.
- Left Rotation we add n times element at the end and remaining element front.
- In Right Rotation we add last n element to the first and reamining element to the last.

```py
def Rotation(array , n , isLeft):
  if isLeft:
    array = array[n:] + array[0:n]
  else:
    array = array[-n:] + array[:-n]
    
  print(array)
```

```py
function_name([1,2,3,4,5,6],2,True) # result
```
