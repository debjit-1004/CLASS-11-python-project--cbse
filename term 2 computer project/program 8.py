#mirror the alphabets from nth position
s=input('Enter a string:\n')
print('Original string',s)
s=s.lower()
n=int(input('Enter the number:\n'))
s1=s[:n-1]
s2=s[n-1:]
s3=''
al='abcdefghijklmnopqrstuvwxyz'
for i in s2:
    for j in al:
        if i==j:
            c=25-al.index(j)
            s3+=al[c]
print('String after mirroring:',s1+s3)
