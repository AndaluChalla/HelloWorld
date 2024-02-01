phone = input("Phone: ")
digits_mapping = {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five"
}
output = ''
for ch in phone:
    output += digits_mapping.get(ch, "!") + " " #### here only if we pass some number out of 1-5 then ! will be given as output
print(output)