---
title: rgb_to_hsl
tags: math,tuple,intermediate
---

Converts RGB value to HSL (hue, saturation, lightness) value.

- Initially, the RGB values are normalized by dividing each of them by 255.
- Out of these normalized values, maximum and minimum values are found and their difference is calculated and stored as `delta`.
- The **lightness** value is calculated by finding the average of the sum of maximum and minimum values.
- The **saturation** value is calculated by dividing `delta` with `1 - |2L - 1|`.
- The **hue** value is calculated based on which of the normalized values is maximum. This is then multiplied by 60 to convert it in degrees.

```py
def rgb_to_hsl(r, g, b):
  r_norm = r / 255
  g_norm = g / 255
  b_norm = b / 255

  color_max = max(r_norm, g_norm, b_norm)
  color_min = min(r_norm, g_norm, b_norm)
  delta = color_max - color_min

  h, s = 0, 0
  l = (color_max + color_min) / 2

  if delta == 0:
    h = 0
    s = 0
  else:
    s = delta / (1 - abs(2 * l - 1))

    if color_max == r_norm:
      h = 60 * (g_norm - b_norm) / delta
    elif color_max == g_norm:
      h = 60 * ((b_norm - r_norm) / delta + 2)
    elif color_max == b_norm:
      h = 60 * ((r_norm - g_norm) / delta + 4)

  h = h if h >= 0 else 360 + h
  return (h, s * 100, l * 100)
```

```py
rgb_to_hsl(30, 50, 100) # (222.85714285714286, 53.846153846153854, 25.49019607843137)
```
