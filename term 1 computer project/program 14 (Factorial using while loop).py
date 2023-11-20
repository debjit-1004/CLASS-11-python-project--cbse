x=int(input('Enter the number whose factorial is needed to be found:'))
factorial=1
while x>0:
    factorial*=x
    x-=1
print('The factorial of ',x,'is',factorial)
