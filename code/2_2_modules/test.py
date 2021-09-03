# -*- coding: utf-8 -*-

import os
from bar import * # or import bar



nb_beer = input("How many beers do you want to drink ? ")
nb_beer = int(nb_beer)

# test of the function order_price

total_price = order_price(nb_beer) # or bar.order_price(nb_beer)
print('Your order of {} beer(s) will cost you {}T'.format(nb_beer, total_price))

os.system('pause')

