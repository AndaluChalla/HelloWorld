full_name= input('enter your full name: ') ## this will ask for user input in the console

body_weight = input('''enter weight in lbs= ''')   # it will ask for input for weight

print(type(body_weight))           # this will print the type of variable (body_weight)

weight_in_kgs = int(body_weight) * 0.45  # here we are converting body_weight string to int and calculating weight in kg's and storing in weight_in_kgs

print('my name is '+ full_name + ' and ' + ' I weigh ' + str( weight_in_kgs ) + ' kg ') # as string only concatenates with string so converting weight_in_kgs to str and concatenating





