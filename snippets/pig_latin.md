---
title: Piglatin    
tags: slicing,intermediate
---

# What Is Pig Latin ???
Pig Latin is a language game or argot in which words in English are altered, usually by adding a fabricated suffix or by moving the onset or initial consonant or consonant cluster of a word to the end of the word and adding a vocalic syllable to create such a suffix.

```py
def pig_latin(text):
	first_word = text[0]
	if first_word in 'aeiou':
		result =  text+'ay'
		
	elif first_word in 'AEIOU':
		result = text+'ay'
				
	else:
		result = text[1:]+first_word+'ay'
		
	return result
```

```py
pig_latin('apple') #applay
pig_latin('banana') #ananabay
```
