---
title: permuterm index
tags: permuterm-index,advanced
---



- Returns the permuterm index in information retrieval

```py
import os

#creating the function that returns parts of string according to the number that inputs
def rotate(str, n):
    return str[n:] + str[:n]

#getting the keyboard input from the user
word = input('Enter Word : ')
#Adding the $ mark for permuterm index
dword = word + "$"

#for loop that call the rotate function in decreasing order of the length of the word inserted by the user
for i in range(len(dword),0,-1):
    output = rotate(dword,i)
    print(output)
    
```

