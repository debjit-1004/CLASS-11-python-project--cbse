n=int(input('Enter the number of lines of floyd triangle to be printed'))
value=int(n*(n+1)/2)
for i in range(n+1, 1,-1):
    for j in range(i,1,-1):
        print(value, end=' ')
        value-=1
    print()
