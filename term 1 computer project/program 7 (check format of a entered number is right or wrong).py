str=input("Enter the number with dash \n")
num=0
dash=0
for i in str:
    if i.isnumeric():
        num+=1
    if i=='-':
        dash+=1
if len(str)==(dash+num) and dash==2 and num==10 and str[3]=='-' and str[7]=='-' :
    print("The number is in correct format")
else:
    print("The number is not in correct format")
