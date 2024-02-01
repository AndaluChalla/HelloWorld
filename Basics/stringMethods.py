
######### INPUT METHOD

Name = input('enter your full name: ')
Birth_Year = input('enter your birt year: ')
print ('My name is ' + Name + ' I am ' + str( 2023 - int(Birth_Year)) + ' years old ')


######### UPPER METHOD

name = ' Vamshi Vardhan Reddy Challa'
upper_name= name.upper()
print(upper_name) ### converts small case to upper case but doesn't replace the original string it stores in a diffent location
print(name)     ### to check the old value is still there

######### LOWER METHOD

name = ' VAMSHI VARDHAN REDDY CHALLA'
lower_name= name.lower()
print(lower_name) ### converts upper case to small case but doesn't replace the original string it stores in a diffent location
print(name)     ### to check the old value is still there


####### FIND method
#### to get the index of a charecter in a string

name = ' VAMSHI VARDHAN REDDY CHALLA'
print(name.find('H'))
print(name.find('VARDHAN'))
print(name.find('v')) ##### it give -1 as result as there is no smallcase v
print(name.replace('VAMSHI','AKSHITHA'))



####### IN OPERATOR ( to check existence of a charecter or a sequence of chars in a string)
#### (produces a boolean value)

name = ' VAMSHI VARDHAN REDDY CHALLA'
print('VAMSHI' in name)










