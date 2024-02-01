numbers = [0,1,2,3]
numbers.append(20) #### to add a number in the list it will add at the last index
print(numbers)
numbers = [0,1,2,3]
numbers.insert(0,20) ### to add in a specific index have to give index first and the number we want to add
print(numbers)
numbers = [0,1,2,3]
numbers.clear() ######### to delete all items in the list
print(numbers)
numbers = [0,1,2,3]
numbers.reverse() ###### to reverse the list
print(numbers)
numbers = [0,1,2,3]
numbers.pop()
print(numbers) ##### to delete the the last item in the list
numbers = [0,1,2,3]
print(numbers.index(0)) ### gives the value at index 0
numbers = [0,1,2,3]
print(50 in numbers) ##### will check the index 50 and gives boolean value
numbers = [0,1,2,3,3,3]
print(numbers.count(2)) ##### gives the cpunt of a specific value in the list
numbers = [0,1,5,2,6,3,10,-1]
numbers.sort()
numbers.reverse()
print(numbers)
numbers = [0,1,2,3]
numbers2= numbers.copy()
numbers.append(10)
print(numbers)
