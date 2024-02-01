numbers = [3,6,21,80,14,10,100]
max = numbers [0] #### giving 0 index and assuming it as a largest number
for number in numbers:
    if number > max:
        max = number
print(max)