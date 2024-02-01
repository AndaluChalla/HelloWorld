try:
    age = int(input('Age: '))
    print(age)
except ZeroDivisionError:
    print('can not divide by zero')
except ValueError:
    print('Invalid Value')

##### for more exception types https://docs.python.org/3/library/exceptions.html