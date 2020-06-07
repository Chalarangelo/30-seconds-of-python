---
title: functionName
tags: array,intermediate
---

Explain briefly what the snippet does.

Explain briefly how the snippet works.

```py
def remExtraSpace(text):
    analysed_text=''''''
    for index,char in enumerate(text):
        if text[index]==" " and text[index+1]==" ":
            pass
        else:
            analysed_text+=char
    return analysed_text
```

```py
text="Hello             World              !" # Will Remove Extra Spaces
text=remExtraSpace(text)
print(text)
```
