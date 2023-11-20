#sum of each row in a m*n matrix
l=[[1,2,3],[4,5,6],[23,5,7]]
row=len(l)
s=0
for i in range(row):
    s=sum(l[i])
    print('Sum of row',i+1,'is :',s)
    s=0
