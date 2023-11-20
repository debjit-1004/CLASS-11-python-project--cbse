#finding the second largest number and duplicate numbers in the list
l=eval(input('enter a list: '))
print('The second largest digit is',max([i for i in l if i!=max(l)]))
z=[]
for a in l:
    n=l.count(a)
    if n>1 and a not in z:
        z.append(a)
print('The repeted elements are:',z)
