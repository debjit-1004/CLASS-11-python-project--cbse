#display 2nd largest no.
#display duplicate no.
#display highest frequency no. in a tuple
t=eval(input('Enter the tuple enclosed in first bracket:\n'))
l=list(t)
print('The second largest number in the tuple is',max([i for i in l if i!=max(l)]))
z=[]
for a in l:
    n=l.count(a)
    if n>1 and a not in z:
        z.append(a)
if len(z)>0:
    print('The repeted elements are:',tuple(z))
else:
    print('There are no repeted elements')
import statistics
print('The number appearing most is',statistics.mode(l))

