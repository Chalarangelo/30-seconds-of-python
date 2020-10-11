---
title: calc_std_drink
tags: math,beginner
---

- Calculate the number of standard alcoholic drinks.

```py
def calc_std_drink(abv, vol):
    alc_vol = abv * vol / 100.
    std_drink = alc_vol / 14.  # 1 std drink = 14 g alcohol
    return std_drink
```

```py
calc_std_drinks(6.5, 330)  # give number of stardard drinks for 330 ml of 6.5% beer
```
