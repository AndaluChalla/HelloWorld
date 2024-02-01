names = ['john', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names[::-1]) #### this reverses the string
print(names[2:4]) ### prints 2-4 but not 4
print(names[2:])#### prints from 2 till end indexing start from 0 so starts from mosh
#### all this returns a new list it doesn't modify the original list
names[0] = 'Jon' ### to update the value at index 0
print(names)