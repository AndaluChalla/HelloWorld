weight = input('Weight: ')
weight_units = input('(L)bs or (K)g : ')
if weight_units.upper() == 'L':
    converted_weight = int(weight) * 0.45
    msg = f'you weigh {converted_weight} Kg'
    print(msg)
else:
    converted_weight = int(weight)/ 0.45
    msg = f'You weigh {converted_weight} pounds'
    print(msg)
