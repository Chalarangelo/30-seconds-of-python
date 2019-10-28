---
title: shift_cipher
tags: encryption,medium
---

The program uses the symmetric key cipher called shift cipher.
It shifts the ascii value of the entered text and shifts it based on a given key.

the `chr` function converts ascii to character and `ord` function converts char to ascii.

```py
def shift_cipher(text,key):
    enc = ' '
    for i in text:
        enc = enc + chr(ord(i)+key)
    return enc
```

```py
a = 'hello'
b = shift_cipher(a,5)
print(b)
```
        
