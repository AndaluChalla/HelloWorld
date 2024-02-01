#### Dictionaries store info in key-value pairs

my_info ={
    "name": "vamshi", ###### Key - Vamshi && Value - Vamshi
    "DOB": "30 years",
    "sex": "male"
}
my_info['name'] = 'Akki' #### we can add key-value pairs easily this way to existing dictionries
print(my_info['name'])
print(my_info.get('Name')) ###### .get will not throw error if the required info is not availabe it will give o/p as NONE
print(my_info.get('city', 'Hyderabad')) ##### we can also peass key and value with .get method
#print(my_info['Name']) #### throws error with msg doesn't exist with same char as N is caps

