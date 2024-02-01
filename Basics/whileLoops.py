'''
i = 1
while i <=5:
    print(i)
    i = i+1 #####or you can write i +=1
print('done')

####### multiplying string here with i

i = 1
while i <=5:
    print('*' * i)
    i = i+1 ##### or you can write i +=1
print('done')

'''

############ Guessing game

secret_number=13
guess_count=0
guess_limit=3
while guess_count < guess_limit:
      guess_number=int(input(f'Guess : '))
      guess_count += 1
      if guess_number==secret_number:
        print('Congrats,you guessed the correct number')
        break
else:
    print('sorry you failed')



command = ""
started = "False"
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car is already started...neku unnadi okate car enni sarlu start chestav musukuni drive chai")
        else:
            started = True
            print('car started.......')
    elif command == "stop":
        if not started:
            print("car is already stopped you stupid don't waste time")
        else:
            started = False
            print('car stopped')
    elif command == "quit":
        print('process exited')
    elif command == "help":
        print(""" 
start - to start the car  
stop - to stop the car
quit - to exit
        """)
    elif command == "quit":
        print('process exited')
        break
    else:
     print("I do not understand your input ")
    









