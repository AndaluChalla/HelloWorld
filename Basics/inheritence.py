class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    def bark(self):
        print('bark')


class Cat(Mammal):
    pass

Dog1 =Dog() ###creating object for dog class
Dog1.bark()
Dog1.walk()

Cat1 = Cat() ### creating object for cat class
Cat1.walk()