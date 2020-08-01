---
title: Circle
tags: maths,beginner
---

Find the Radius, Area or Circumfrence of a Circle using any of three Area, Radius or Circumfrence.

It simply takes your input uses the formula and returns you the answer, there is a function ```Find(what, using, value)``` you have to fill what you want to find what you are using to find it and the value of what are you using. function takes Strings as input ```R``` for Radius, ```A``` for Area, ```C``` for Circumfrence.

```py
import math

Radius = 0
Circumfrence = 0
Area = 0

PI = 3.141592653589793238
#Change the accuracy of PI according to need


def Find(what,using,value):

  #Area
  if(what == 'A'):
    
    if (using == 'R'):
      Radius = value
      return PI*(Radius*Radius)

    elif (using == 'C'):
      Circumfrence = value
      Radius = Circumfrence/2*PI
      return PI*(Radius*Radius)
      
  #Radius
  elif (what == 'R'):

    if (using == 'A'):
      Area = value
      return math.sqrt(Area/PI)

    elif (using == 'C'):
      Circumfrence = value
      return Circumfrence/2*PI
      
  
  #Circumfrence
  elif (what == 'C'):

    if (using == 'A'):
      Area = value
      Radius = math.sqrt(Area/PI)
      return 2*PI*Radius

    elif (using == 'R'):
      Radius = value
      return 2*PI*Radius
```

```py
print(Find('C','A',7854)) #result : 314.1596326792749

#use strings to specify what you want
# A for Area 
# R for Radius 
# C for Circumfrence
```
