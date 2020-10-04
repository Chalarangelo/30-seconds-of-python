---
title: Slope and Equation of a Line
tags: math, intermediate
---

Explain briefly what the snippet does.

- Calculates the slope and equation of a line in slope intercept form from two points.
- Calculates the slope (Δy/Δx) and the y-intercept (y₁ - (x₁ * m))

```py
def SlopeAndEquation(x1, y1, x2, y2):
  slope = (y2-y1)/(x2-x1)
  yIntercept = y1-(x1*slope)
  return {"slope": slope, "Equation": "y = {}x {} {}".format(slope, '-' if yIntercept < 0 else '+',  abs(yIntercept))}
```

```py
SlopeAndEquation(9,3,1,1) # {'slope': 0.25, 'Equation': 'y = 0.25x + 0.75'}
```
