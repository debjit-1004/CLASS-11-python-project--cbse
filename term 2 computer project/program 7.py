#Nos comming consequetively 3 times
l=eval(input('enter the list:\n'))
for i in range(len(l)-2):
    if l[i+1]==l[i] and l[i+2]==l[i]:
        print('The number comming three times consecutively is:',l[i])
