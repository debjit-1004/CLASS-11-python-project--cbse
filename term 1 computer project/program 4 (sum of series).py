# program to print the sum of the series 1+(x/1)+(x^2/2)+(x^3/3)....(x^n/n)
x=int(input('enter the value of x'))
n=int(input('enter the value of n'))
s=1
for i in range(1,n+1):
    s=s+pow(x,i)/i
print(s)
