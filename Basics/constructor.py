##### A Constructor is a fucntion called  at the time of creating an object
'''

class Point:
    def __init__(self, x, y): #### here what is written after def is the constructor so we are defining a constructor to pass required values while creating the object
                self.x = x ### self is reference to the current object so like we wrote in classes.py code instead of writing point1.x we are defining them in the constructor
                self.y = y
    def move(self):
        print('move')
    def draw(self):
        print('draw')


point = Point(10, 20)
print(point.x, point.y)
'''
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person('John Smith')
vamshi= Person('Steamship Challa')
john.talk()
vamshi.talk()
