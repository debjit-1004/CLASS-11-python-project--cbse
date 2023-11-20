i=int(input("Enter the limit"))
c=0
print('The prime numbers less than ", i ,"is :')

for a in range(2,i):
    for b in range(2,a):
        if a%b==0:
            c+=1

    if(c==0):
        print(a)
    c=0
    
