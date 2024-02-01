### we use classes to define new types,,, basically a group of different type of objects like int, string, bool, lists, dictioneris etc
#### An object is an instance of a class
#### class defines the blueprints for creating objects .....objects are actual instances of the class blueprints

class Point: ##### defined a class with the name Point ane class name always start with cap letter and each of the combining letter for ex PointSystem
    def move(self): ###### defining a function for Point class
        print('move')
    def draw(self): ###### defining a function for Point class
        print('draw')


point1 = Point() ## we are calling Point class here like a functions which creates a new object and returns it and we storing it in point1 variable
                ## and we can create as many objects as we want in below point1 is one and point2 is 2nd
point1.draw() #### we can access the function we created in the class like here
point1.x= 10
point1.y= 20
print(point1.x)

point2 = Point()
print(point2.x) ### this throws error as there is no atribute x for point2 object (actual error: AttributeError: 'Point' object has no attribute 'x')
                #### each object is different isntance of it's class







