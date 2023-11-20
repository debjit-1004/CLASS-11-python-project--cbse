#display is's starting with 91
n=int(input('Enter the number of users:\n'))
d={}
l=[]
for i in range(n):
    i_d=int(input('Enter the
                  id:\n'))
    d[i_d]=input('Enter the name:\n')
k=d.keys()
print("The id's starting with 91's are:")
for j in k:
    if str(j)[0:2]=='91':
        l.append(j)
print(l)
