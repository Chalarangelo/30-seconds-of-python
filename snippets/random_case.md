---
title: random_case
tags: string,begginer
---

Converts a string to random case.

- Map the string with lambda
- Generate random float from 0 to 1
- Make character upper case if float is lower than `upper_probability`
- If not, make it lower case

Default `upper_probability` is set to `0.5`, so (on averge), half characters will be upper and half lower.
If you set it to `0.75`, then 75% of characters will be upper-case, etc.

```py
import random

def random_case(s, upper_probability=0.5):
  return ''.join(
    map(
      lambda x: x.upper() if random.random() < percentage else x.lower(),
      s
    )
  )
```

```py
random_case("This is some text") # 'ThIS IS somE tEXt'
random_case("Okay so this is like really nice big example text") # 'okAy sO thIs Is liKE REALlY niCe biG eXAmPle teXT'
random_case("This will be fully upper", 1) # 'THIS WILL BE FULLY UPPER'
random_case("This will be fully lower", 0) # 'this will be fully lower'
random_case("This will be (on averge) 20% upper case", 0.2) # 'this will be (On avergE) 25% uppER case'
random_case("This will be (on averge) 80% upper case", 0.8) # 'ThIS WIlL bE (ON AvERGE) 80% UPPeR CASE'
```
