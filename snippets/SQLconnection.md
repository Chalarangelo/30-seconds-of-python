---
title: SQL connection
tags: SQL,beginner
---

Connects to a SQL database.

- `db = mysql.connector.connect` is used to create the connection to the database
<br>`User` refers to your account's username.
<br>`Password` refers to your account's password.
<br>`Host` refers to the web address of the database.
<br>`Database` refers to the name of the database.
- `cur` will then be used to execute commands
ex.: `cur.execute("SELECT * FROM DATABASE")`

```py
import mysql.connector

db = mysql.connector.connect(user='usr', password='pass', host='host', database='db')
cur = db.cursor()
```
