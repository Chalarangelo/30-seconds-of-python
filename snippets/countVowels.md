---
title:  countVowels
tags: string,beginner
---

Returns number of vowels in the provided string.

We will store all the vowels ('A','a','E','e','I','i','O','o','U','u') in a string.
Then pick every character from the enquired string and check whether it is in the vowel string or not.
If the vowel is encountered then `numVowels` gets incremented.

```py
def countVowels(string):
    numVowels=0
    for char in string:
        if char in "aeiouAEIOU":
           numVowels = numVowels+1
    return numVowels
```

```py
countVowels("Hello Vowels!!")  #4
```
