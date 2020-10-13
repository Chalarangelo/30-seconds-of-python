---
title: fizzbuzz
tags: intermediate, loop
---

Explain briefly what the snippet does.

- A common Python coding challenge
- Here is one way to solve the FizzBuzz challenge
- Challenge: if an input number is divisible by 3, print fizz. If it's divisible by 5, print buzz. And if it's divisible by both 3 and 5, print FizzBuzz.
- Using if statements to iterate over an input number
- The most important thing with this function, is the order of the if statements
- If statements are prioritised by order. For example, if something is divisible by 3 and 5, but that if statement was at the end of the loop, you would only return 3

```py
import sys
inputs = sys.argv
inputs.pop(0)
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print ('fizzbuzz')
    elif n % 3 == 0:
        print ('fizz')
    elif n % 5 == 0:
        print ('buzz')
    else:
        print(n)
# input function
for input in inputs:
    input = int(input)
    fizzbuzz(input)
