#no. of elements
s=input('Enter a string:
        \n')
d={}
c=0
for i in s:
    for j in s:
        if i==j:
            c+=1
    d[i]=c
    c=0
print(d)
