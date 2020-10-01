---
title: copy_to_clipboard
tags: utility,intermediate
---

Copies the content of the variable to clipboard

- Install pyperclip module by `pip install pyperclip`
- Import pyperclip to your program by `import pyperclip`

```py
def copy_to_clipboard(myString):
  pyperclip.copy(myString)
  return 0
```

```py
copy_to_clipboard("Hey, my name is Shreya!") 
```
