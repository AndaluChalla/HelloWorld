quotation = input('enter your quote : ')
vowels = ['a','e','i','o','u']
count = 0
for vowel in quotation:
    if vowel.lower() in vowels:
            count +=1
print(f'number of vowels: {count}')




