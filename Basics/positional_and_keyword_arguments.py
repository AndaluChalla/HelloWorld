def greet_user(first_name, last_name):
    print(f"Hello {first_name} {last_name}!")
    print("Welcome aboard")


print("Start")
greet_user("Vamshi" , "Challa")  ##### these are positional arguments
greet_user("Vamshi" , last_name="Challa") ###### vamshi is the positional argument and last name is the keyword argument as we are passing the value with the keyword
greet_user(first_name="Akshitha" , last_name="Challa")
print("End")

''' we should always use positional arguments first as that is the rule set by python we can also use keyword arguments first but there should be some extra lines opf code you have to write check chatgpt for understanding def greet_user(name): here name is called parameter(parameters are the place holders for the functions)
 here greet_user("Vamshi") Vamshi is the argument we pass to the function
positionsal arguments and keyword arguments.....the way parameters are defined in the function we have to pass arguments in the same order
those are called positional arguments and if we pass arguments with the key(which is parameter) those are keyword arguments
 for keyword arguments position doesn't really matter
 when we pass numerical values user will have hard time understanding when we pass positional arguments'''