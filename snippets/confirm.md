---
title: confirm
tags: utility,beginner,input
---

Continuously prompts user at command line until they enter yes or no

- confirm() takes in a str argument (called message) that is displayed on each iteration
- Returns True when someone inputs y or yes and False when n or no

```py
def confirm(message):
  validators, invalidators= ["y", "yes"], ["n", "no"]
  while 1:
    response = input(message + "(y or n): ")
    if response.lower().strip() in validators:
        return True
    elif response.lower().strip() in invalidators:
        return False
    else:
        print("Please respond with either yes or no")
```


```py
confirm("Do you want fries with that?")
"""
Do you want fries with that?(y or n): f
Please respond with either yes or no
Do you want fries with that?(y or n): y # Returns True
"""

confirm("Do you want fries with that?")
"""
Do you want fries with that?(y or n): n # Returns False
"""
```