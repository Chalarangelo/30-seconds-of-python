---
title: Ajax Request Handler
tags: Python, Django, Ajax, Utility, Ajax View
---

Accepts Ajax request from the code-snippet Django-Ajax-Request which you can find in the git repo of 30-seocnds-of-code (Javascript) and returns HttpResposne in content type of json.

- Import Json to convert your reposne dictionary into string and send to javascript as a promise.
- Handles Request without the refreshment of the page.
- Does not rquire any pip install other than Django.

```py
import json
from django.views import View
from django.http import HttpResponse

# Django View to handle ajax request
class AjaxHandler(View):

  # Handle Get request
  def get(self, request):
  # Get your data here
    body = json.loads(request.body) # This gives a python dictionary
    val1 = body.get("query", "")
    # Similary get values
    # View Logic here
    return HttpResponse(json.dumps({"response": "your_response"}), content_type=application/json)

  # Hnadle Post Request
  def post(self, request):
    # Get your data here
    body = json.loads(request.body) # This gives a python dictionary
    val1 = body.get("query", "")
    # Similary get values
    # View Logic here
    return HttpResponse(json.dumps({"response": "your_response"}), content_type=application/json)

  # Similar for PUT AND DELETE

```
