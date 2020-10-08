---
title: yamlToJson
tags: utility,yaml,json
---

Explain briefly what the snippet does.

- converts given yaml file to json file
- pass yaml file path and expected JSON file path as arguments


```py
import yaml
import json

def yamlToJson(ypath,jpath):
  with open(ypath) as yfile:
    obj = yaml.load(yfile,Loader=yaml.FullLoader)

  with open(jpath,'w') as jfile:
    json.dump(obj,jfile)

  return 0
```

```py
yamlToJson(yamlPath,jsonPath) # yaml file is converted to json
```
