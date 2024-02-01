import ecommerce.shipping ### here we are importing ecommerce package and shipping module with this way code is repeating everytime we call a function
ecommerce.shipping.calc_shipping()
ecommerce.shipping.cal_cost()

# or we can also import specific function like below

from ecommerce.shipping import  calc_shipping, cal_cost
### now we can directly call the function and if we have multiple function we can call them by ',' separator
calc_shipping()
cal_cost()

### or we can call the whole module and access the functions
from ecommerce import shipping
shipping.calc_shipping()
shipping.cal_cost()

