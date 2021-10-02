---
title: bitwise_encription
tags: encrypt, decrypt, biteise,ord
firstSeen: 2021-10-02T17:00:00-06:00
---

- Encrypts a text string with a user-defined password
- Use `ord` in python to convert a character to unicode and thus achieve encryption of your text.
- Encrypt a text string bitwise
- To decrypt, do the same

```py
    def bitwise_encription(content, password):
        encryptedContent , count = [], 0
        for i in content:
            encryptedContent += [chr(ord(i) ^ ord(password[count %len(password)]))]
            count += 1
        return "".join(encryptedContent)
```



```py
en = bitwise_encription("Hello world","my_password") # %3S▒
de = bitwise_encription(en,"my_password") # Hello world
```
