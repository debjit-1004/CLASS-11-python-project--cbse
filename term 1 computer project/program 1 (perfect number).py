#special number eg 6 factors 1,2,3 except itself sum =1+2+3=6
x= int(input('enter the number'))
i=1
s=0
while(i<x):
    if x%i==0:
        s+=i
    i+=1
if s==x:
    print('perfect number')
else:
    print('not a perfect number')
    