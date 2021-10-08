---
title: fahrenheit_to_kelvin
tags: math, beginner
firstSeen: 2021-10-07 09:30:00−05:00
---

Converts temperature from Fahrenheit to Kelvin.
- Follows the conversion formula: `K = (F − 32) × 5/9 + 273.15`.

```py
def fahrenheit_to_kelvin(temp_input):
    return ((temp_input - 32) * 5/9) + 273.15
```

```py
fahrenheit_to_kelvin(32) #273.15
```