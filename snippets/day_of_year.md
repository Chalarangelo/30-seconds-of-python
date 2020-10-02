---
title: day_of_year
tags: utility,beginner
---

The snippet calculates the day of year when date is provided in"YYYY-MM-DD" format.
 - Suppose D is an array of day count like [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
 - Convert the date into list of year, month and day
 - If the year is leap year then set date D[2] = 29
 - Add up the day count up to the month mm – 1. and day count after that.
    
 ```python
 def dayOfYear(date):
    # Convert the date into list of year, month and day
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d = list(map(int, date.split("-")))
    if d[0] % 400 == 0:  # if the year is leap year then set date D[2] = 29
        days[2] += 1
    elif d[0] % 4 == 0 and d[0] % 100 != 0:  # if the year is leap year then set date D[2] = 29
        days[2] += 1
    if(days[int(date[5:7])]<int(date[-2:])): # Checking The Date Given Corresponds to the month.
        return("WRONG DATE!!")
    for i in range(1, len(days)):
        # Add up the day count up to the month mm – 1. and day count after that.
        days[i] += days[i-1]
    print(days[d[1]-1]+d[2])
 ```
 ```python
 dayOfYear("2020-09-30")#274
 ```
