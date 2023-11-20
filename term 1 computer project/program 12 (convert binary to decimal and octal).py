binary=(input("enter the binary number"))
binary=binary.strip()
power=len(binary)-1
decimal=0
for i in range (len(binary)):
    decimal+=int(binary[i])*(2**power)
    power-=1
octal=str(oct(decimal))
print(octal[2:])
print(decimal)
           
