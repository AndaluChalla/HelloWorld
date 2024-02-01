for item in 'Python':
    print(item)

Grades = ['A', 'B','C' ]
for results in Grades:
    print(results)

for item in range(10): ########## The range() function in Python is used to generate a sequence of numbers. It is commonly used in for loops to iterate over a specific range of values. The range() function can be used in three different ways:
    print(item)

for item in range(5,15,2):  #### here 3 is called STEP, where default step is 1 but we want every third consecutive number so we are giving 3  as step.
    print(item)

####### finding the total price
prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")####### this statement is out of for loop if it is inside it prints for each iteration









