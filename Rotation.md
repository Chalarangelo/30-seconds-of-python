---
title: Rotation
tags: python,list_slicing,Rotation
---

This is the shortest method for doing Left or Right rotation.

- We have to pass array, how times rotation which is n and bool value isLeft. For Left Rotation it is True and for Right it is False.
- Left Rotation we add 0 to n element from the first add at the end of list and remaining element to the front.
- In Right Rotation we add last to n element to the first and reamining element to the last.

```py
def Rotation(array , n , isLeft):
  if isLeft:
    array = array[n:] + array[0:n]
  else:
    array = array[-n:] + array[:-n]
    
  print(array)
```

```py
Rotation([1,2,3,4,5,6],2,True) # Left Rotation
Rotation([1,2,3,4,5,6],2,False) # Right Rotation
```
