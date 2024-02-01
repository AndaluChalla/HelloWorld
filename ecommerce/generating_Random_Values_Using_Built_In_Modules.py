import random

# generates random values form 0-1

for i in range(3):
    print(random.random())

# if we want values in specific range code like below using randit() function

for i in range(3):
    print(random.randint(10,30))

# to pick a random string
members = ['Vamshi','Akki','John', 'Joe']
Leader = random.choice(members)
print("Leader for this team is " + Leader)

# create a class called DICE and ROll method to o/p tuple


class Dice:
    def roll(self):
        first = random.randint(1,6)
        second= random.randint(1,6)
        return first, second ### for returning a tuple you don't have to add them in a paranthesis or square brackets


dice = Dice()
print(dice.roll())

