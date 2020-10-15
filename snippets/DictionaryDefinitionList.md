---
title: Dictionary.com word definition checker
tags: list,urllib,beginner
---



- Returns definitions of the words in the list cald word

```py
import pandas as pd 

#creates a list of the word that needs to be searched in dictionary.com
word = ['handy','whisper','lovely','scrape']

List = []

#creates a for loop to pull the definitions for each word in the list
for i in range(0,4):
    url = "https://www.dictionary.com/browse/" + word[i] + ""
    #urllib was used to pull the whole html page according to word
    htmlfile = urllib.request.urlopen(url)
    soup = BeautifulSoup(htmlfile, 'lxml')
    #beautifulsoup was used to extarct only the definition from the html file
    soup1 = soup.find(class_="one-click-content css-1p89gle e1q3nk1v4")
    soup1 = soup1.get_text()
    #appended the definitions into a list according to the order 
    List.append([word[i],soup1])

#Words and Definition lists are added into a dataframe
df = pd.DataFrame(List, columns=["Word", "Definition"]) 

print(df)
```


