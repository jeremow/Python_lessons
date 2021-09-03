# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 10:47:23 2021

@author: jeremow

Main algorithm of the karaoke bar
"""

from functions import *
from data import *

# Variables to exit the while-loop
count_songs = 0
stay_answer = True

# Initialize the list for songs
waiting_list = []

# Initialize the dict for users, we will save the bill next to the name
users = create_users()

while count_songs < max_songs and stay_answer:

    add_songs(waiting_list, count_songs)

    if count_songs % 3 == 0:
        order_drinks(users)

    try:
        print('\nNext song is {}, get ready!'.format(waiting_list[0]))
        waiting_list.pop(0)
        count_songs += 1
    except IndexError:
        print('\nThere is no song in the waiting list !\n')

    input('Push enter to finish the song...')

    stay_answer = input('Do you want to continue to sing? [y]/n ')

    if stay_answer.lower() == 'n':
        stay_answer = False
    else:
        stay_answer = True

total_price = get_bill(users)

print('----------\n'
      'Thank you for your visit and see you soon!')
