price_footwear=float(input('Enter the cost of footwear \n'))
item_f=int(input('Enter the number of footwear sold \n '))
if price_footwear <=500:
    CGST_f=0.05*price_footwear*item_f
    SGST_f=CGST_f
    print('The rate of CGST and SGST is 5% for each and for each pair of shoes')
else:
    CGST_f=0.18*price_footwear*item_f
    SGST_f=CGST_f
    print('The rate of CGST and SGST is 5% for each and for each pair of shoes')
print('The total selling price is ',(2*CGST_f +price_footwear))
print('The CGST  leived  is ', CGST_f)
print('The total SGST leived is ',SGST_f)
print()
price_apparels =float(input('Enter the cost of apparels \n'))
item_a =int(input('Enter the number of apparels sold \n '))
if price_apparels <=1000 :
    CGST_a=0.05*price_apparels*item_a
    SGST_a=CGST_a
    print('The rate of CGST and SGST is 5% for each and for each pair of shoes')
else:
    CGST_a=0.12*price_apparels*item_a
    SGST_a=CGST_a
    print('The rate of CGST and SGST is 5% for each and for each pair of shoes')
print('The total selling price is ',(2*CGST_a +price_apparels))
print('The total CGST  leived  is ', CGST_a)
print('The total SGST leived is ',SGST_a)


