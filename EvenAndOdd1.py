print("Make your list")
a=[0,0,0,0,0]
even=[0,0,0,0,0]
odd=[0,0,0,0,0]
e=0
o=0
for i in range(0,5):
    a[i]=int(input("Enter element"))
    if(a[i]%2==0):
        even[e]=a[i]
        e=e+1
        continue
    else:
        odd[o]=a[i]
        o=o+1
print("Even Numbers")
for i in even:
    print(i)
print("Odd Numbers")
for i in odd:
    print(i)
