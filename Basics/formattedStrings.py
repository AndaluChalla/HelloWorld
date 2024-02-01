# requirement is to print Vamshi [Challa] is a coder, so we use formatted string concept to simplify the code

##normal way to write the code

first = 'Vamshi'
last = 'Challa'
message = first + ' [' + last + '] is a coder'
print(message)

### writing the same with formatted strings

first = 'Vamshi'
last = 'Challa'
msg = f'{first} [{last}] is a coder'
print(msg)

