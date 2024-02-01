coordinates = (1,2,3)
##### to get the values in the coordinate tuple we write code like below

print(coordinates[0] * coordinates[1] * coordinates[2])

### or

x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
print(x*y*z)

##### with unpacking

x,y,z = coordinates ### this is not limited to tuples we can use it for lists aswell below is the example
print(x*y*z)

#### unpacking with LISTS
coordinates = [1,2,3]
x,y,z = coordinates
print(x*y*z)