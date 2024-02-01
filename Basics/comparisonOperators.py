temperature = input('enter the current temperature in Centigrade : ')
if int(temperature) >=30:
    print("it's a hot day")
else:
    print("it's not a hot day")

####### checking name length

name = input('please enter your full name : ')
name_length = len(name)
if name_length <=3 or name_length >= 15:
    msg = f'Error: entered length is {name_length} , name must be atleast 3 charecters and maximum of 16 charecters '
    print(msg)
else:
    print('name stored successfully')



