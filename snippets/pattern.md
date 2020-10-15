# Number Pattern using python Logic

```
To get the reslut as of the pattern like
4
112
322
334
544
```

```
def pattern():
    n = int(input())
    x, y = [], []
    r = []
    for i in range(1, n+1):
        if i % 2 == 0:
            x.append(i)
        else:
            y.append(i)
   # print(x, y)
    p1, p2 = [], []
    for j in y:
        a = j
        b = j + 1
        c = str(a) * (n - 2) + str(b)
        p1.append(c)
    for j in x:
        a1 = j + 1
        b1 = j
        c1 = str(a1) + str(b1) * (n-2)
        p2.append(c1)
    for i in range(round(n/2)):
        r.append(p1[i])
        r.append(p2[i])
    print("\n".join(r))
pattern()
```

```
Output:
6
11112
32222
33334
54444
55556
76666
```


