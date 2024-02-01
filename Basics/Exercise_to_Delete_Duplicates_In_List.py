numbers =[10,12,11,11,12,13,14,14,14,15,16,19,19,13,12,18,20]
uniques =[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
        uniques.sort()
print(uniques)




