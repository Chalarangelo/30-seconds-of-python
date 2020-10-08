---
title: slice_uname_domain
tags: string, tuple, beginner
---
Slices username and domain from an email address.

- Uses email_add.split("@")[0] to get the string before "@".
- Uses email_add.split("@")[1] to get the string after "@".
- Returns a tuple of the above two obtained values.

```py
def slice_uname_domain(email_add):
  return (email_add.split("@")[0], email_add.split("@")[1])
```

```py
slice_uname_domain("thevirtualbuddy@gmail.com") # ('thevirtualbuddy', 'gmail.com')
```
