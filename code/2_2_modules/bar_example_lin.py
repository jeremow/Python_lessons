#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

import os # this library is useful to communicate the operating system of your computer

# we define our function to get the order price :

def order_price(nb_beer, price_beer=4000):
    """
    Function which returns the price of a specific order of beers
    
    (nb_beer >= 0)
    """
    return nb_beer * price_beer

nb_beer = input("How many beers do you want to drink ? ") # asking the user to give his order

nb_beer = int(nb_beer) # convert

total_price = order_price(nb_beer) # compute the price

print('Your order of {} beer(s) will cost you {}T'.format(nb_beer, total_price))

os.system('pause') # this line is used by Windows to avoid quitting the terminal when you launch it