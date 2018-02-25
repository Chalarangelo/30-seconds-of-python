## subsetfromsum

A snippet which returns a subset(2 numbers) from an array which equals to given sum.

## Implementation
```python
numlist = [3,35,8,12,6,4]
sum = 9
validated = []
isthere=[]

def doverification():
    for i in numlist:
        if(i<sum):
            validated.append(i)
        else:
            print('number < sum')

doverification()

l=1
def doappending():
    for k in validated:
        for l in validated:
            if(l + k == sum):
                print('Its a match')
                if l not in isthere:
                    isthere.append(l)
                    isthere.append(k)
                else:
                    continue
            else:
                print(' Not a match')


doappending()

```

## Example
```python
numlist = [3,35,8,12,6,4]
sum = 9
validated = []
isthere=[]

def doverification():
    for i in numlist:
        if(i<sum):
            validated.append(i)
        else:
            print('no <9')

doverification()

l=1
def doappending():
    for k in validated:
        for l in validated:
            if(l + k == sum):
                print('Its a match')
                if l not in isthere:
                    isthere.append(l)
                    isthere.append(k)
                else:
                    continue
            else:
                print(' Not a match')


doappending()
print(isthere) # [6, 3]

```
