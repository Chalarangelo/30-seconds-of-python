---
title: list_of_words
tags: list, beginner
---

Returns the list of words from the given sentence.

Use `split()` to split a string into a list by the specifying a separator as its parameter.

```py
def list_of_words(sentence):
  return sentence.split(' ')
```

```py
my_sentence = "I Love Python"
list_of_words(my_sentence) # ['I', 'Love', 'Python']
```