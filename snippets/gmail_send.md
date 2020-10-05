---
title: gmail_send
tags: utility, beginner
---

gmail send is used send an email using python throught gmail smtp

```py
import smptlip
def gmail_send(receiver_email, gmail_password, sender_email, message):
  
    # Specifying the from and to addresses

  fromaddr = sender_email
  toaddrs  = receiver_email

  # Writing the message (this message will appear in the email)

  msg = message

  # Gmail Login

  username = sender_email
  password = password

  # Sending the mail  

  server = smtplib.SMTP('smtp.gmail.com:587')
  server.starttls()
  server.login(username, password)
  try:
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
    return f"Email sent to {toaddrs} from {fromaddr}".
  except Exception as e:
    return e
```

```py
gmail_send("a@b.com", "xxxxxxxx", "b@c.com", "Hello World")
```
