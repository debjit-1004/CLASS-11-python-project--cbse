#find list with max elements and find union of both lists
l1=eval(input('Enter the list in third brackets separated by a comma:\n'))
l2=eval(input('Enter the list as instructed previously:\n'))
if len(l1)>len(l2):
    print('The list with maximum number of elements is:',l1)
elif len(l2)>len(l1):
    print('The list with maximum number of elements is:',l2)
else:
    print('Both list have the same number of elements')
print('The union of the two lists is:',l1+l2)
