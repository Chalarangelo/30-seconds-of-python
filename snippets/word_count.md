---
title: word_count
tags: string,beginner
firstSeen: 2021-07-18T08:14:11+0000
lastUpdated: 2021-07-18T08:14:11+0000
---

Calculates the total number of occurence of a word in a given string .

- Uses `.split()` method to give a list of words from the string , which are used by `collections.Counter()` method to find the total occurences of a word in that string .

```py
from collections import Counter 

def word_count(query, string):
  words = string.split()
  counter = Counter(words)
  return counter[query]
```

```py
string = "cup infront of a cup behind another cup"
word = "cup"

def word_count(word, string) # 3
```
