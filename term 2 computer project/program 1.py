#moving the zeros at the end of the list
l=eval(input('Enter a list in third brackets separated by commas :\n'))
print("List before moving the zeros to the end: ",l)
for i in l:
    if i==0:
        l.remove(i)
        l.append(0)
print('List after moving the zeros to the end:',l)

