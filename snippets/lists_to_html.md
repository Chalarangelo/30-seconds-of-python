---
title: lists_to_html
tags: list,html,function,table
---

Builds the HTML file, which is drawn based on the imported dict.

```py
import pandas as pd
import random

def list_to_html(dataframe):
    df = pd.DataFrame(dataframe)
    filename = "converted-"+str(random.randint(1111,5555))+".html"
    df.to_html(
        filename
        ,encoding="UTF-8"
    )
    return filename
  
```

```py
list1 = ["One", "Two", "Three"]
list2 = ["David", "Jason", "Jackson""]
list_to_html({"numbers":list1, "names":list2}) # converted-1569.html
```
