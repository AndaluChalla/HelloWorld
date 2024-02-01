is_hot = False #### boolean value should always start with a Caps letter
is_cold = False

if is_hot:
    print('It is a hot day') ###### this statement is in the if condition as there is a space before print
    print('Stay Hydrated')
elif is_cold:
    print('It is a cold day')
    print('keep warm')
else:
    print("It's a Lovely day")

print('Enjoy your day') ###### this statement is not in the if condition

import time

########## EXAMPLE
import webbrowser
url = "https://www.realtor.com/realestateandhomes-detail/105-Winchester-Cv_Madison_MS_39110_M84446-28449"
Area_of_interest = input("enter the area you are looking to buy a property in: ")
print(f"Great {Area_of_interest} is a great locality to own a property, we are glad to help you with the process")
home_value = input('Please enter your budget USD: $ ')
print(f'great in {home_value} range we have couple of houses available')
CreditScore = input('to determine the down payment please enter your credit score between 450 & 850: ')
if int(CreditScore) >= 720:
    CreditScore = 'Good'
    down_payment = (10 / 100) * int(home_value)
    print(f"Your credit score is {CreditScore} your Down Payment is : $ {down_payment}")
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    time.sleep(1)
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    time.sleep(1)
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    time.sleep(1)
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Redirecting to the property page')
    time.sleep(2)
    webbrowser.open(url)
else:
    CreditScore = 'Bad'
    down_payment = (20 / 100) * int(home_value)
    print(f"Your credit score is {CreditScore} your Down Payment is : $ {down_payment}")   ##### used formatted string's here instead of conversting down_paymenht value to str like in the previous print stmnt)
    print('>>>>>>>>>>>>>>Redirecting to the property page')
    print(f"Your credit score is {CreditScore} your Down Payment is : $ {down_payment}")
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    time.sleep(1)
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    time.sleep(1)
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    time.sleep(1)
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Redirecting to the property page')
    time.sleep(2)
    webbrowser.open(url)

print("Please contact us for any questions ")

