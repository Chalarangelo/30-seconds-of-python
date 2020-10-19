---
title: capitalize_every_second_character
tags: utility, beginner
---

Gives the sentence a sarcastic tone by capitalizing every second character

- Itterates over the upper cased sentence, lowers every 2nd character.
- ''.join() Joins the characters filter using the conditionals above.

```py
def capitalize_every_second_character(string):

  return ''.join(c.lower() if index%2==0 else c for index, c in enumerate(string.upper()))
```

```py
capitalize_every_second_character('yeah like that would work!') # 'yEaH LiKe tHaT WoUlD WoRk!'
```
