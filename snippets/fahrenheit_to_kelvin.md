|title|tags|unlisted|firstSeen|lastUpdated|
|----|----|-----|-----|-----|
|fahrenheit_to_kelvin|math,beginner|true|2021-10-01T02:06:03+05:00|2021-10-01T02:06:03+05:00|


Converts Fahrenheit to Kelvin.

- Follow the conversion formula `K = 5/9 * (F - 32) + 273`.

```py
def fahrenheit_to_kelvin(degrees):
  return ((5/9)*(degrees - 32) + 273)
```

```py
fahrenheit_to_kelvin(32) # 273.0
```