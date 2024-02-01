########## and operator

hash_high_income = True
has_good_credit = True

if hash_high_income and has_good_credit:
    print("you are eligible for loan") ##### o/p is because both are true FOR AND OPERATOR both the values should be true

########## or operator

hash_high_income = True
has_good_credit = False

if hash_high_income or has_good_credit:
    print("you are eligible for loan") ##### o/p is because one is true FOR OR OPERATOR any of the values should be true


######### not operator

hash_criminal_record = False
has_good_credit = True

if has_good_credit and not hash_criminal_record:
    print("you are eligible for loan") ##### o/p is because has criminal record is converted to ture by not operator though the value is False



