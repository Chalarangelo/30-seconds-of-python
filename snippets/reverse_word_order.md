---
title: Reverse Order of Words in String
tags: string,beginner
---

Python program that reverses the order of words in the given sentence.

- Firstly, using split() we store the individual words in the sentence in a variable
- Next, we splice the list of words and set the step as -1 which will print it in a reverse manner. 

```py
def reverseWords(my_sentence):
    my_list = my_sentence.split()
    print(' '.join(my_list[::-1])) 
```

```py
my_sentence = "Lazy Brown Fox"
reverseWords(my_sentence) # Fox Brown Lazy
```
