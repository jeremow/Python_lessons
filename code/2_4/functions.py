# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 10:45:22 2021

@author: jeremow

Useful functions for the karaoke bar algorithm
"""

from data import *
from random import choice


def create_users(max_users=5):
    """
    Ask the leader how many there are and the names of each.

    Returns
    -------
    users: dict.

    """

    users = {}

    print('Welcome to UB KARAOKE\n-------------')

    nb_users = int(input('How many people will sing? (Min: 1, Max: {}) :\n'.format(max_users)))

    while nb_users < 1 or nb_users > max_users:
        nb_users = int(input('Sorry, not possible. How many people will sing? (Min: 1, Max: {})'.format(max_users)))

    print('\nHere we go for their names, give one by one.')

    for i in range(1, nb_users + 1):
        name = input('User {}: '.format(i))
        users[name] = 0

    print('\nThank you and have a great evening.')

    return users


def add_songs(waiting_list, count_songs):
    """
    Adding songs to the waiting list of the karaoke

    Parameters
    ----------
    waiting_list : TYPE
        DESCRIPTION.
    count_songs : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """

    print('The list of songs :\n-----------')

    for key, value in songs.items():
        print(key, ':', value)

    nb_songs = len(waiting_list) + count_songs
    remaining_songs = max_songs - nb_songs

    nb_add_songs = int(input(
        'There are {} remaining songs before leaving.\nHow many songs to you want to add? '.format(remaining_songs)))

    while nb_add_songs < 0 or nb_add_songs > remaining_songs:
        nb_add_songs = int(input(
            'Sorry, value is not possible.\nThere are {} remaining songs before leaving.\n'
            'How many songs to you want to add? '.format(remaining_songs)))

    i = 0
    while i < nb_add_songs:
        try:
            i_song = int(input('Write the number of the song (0 for random): '))
            if i_song == 0:
                waiting_list.append(choice(songs))
            else:
                waiting_list.append(songs[i_song])
            i += 1
        except KeyError:
            print('Sorry, the number of song is incorrect.')
        except ValueError:
            print('Sorry, this is not a number.')

    print('\nWaiting list is now:\n----------')

    for song in waiting_list:
        print(song)


def order_drinks(users):
    """
    Order drinks to the barman/maid

    Parameters
    ----------
    users : DICT
        DESCRIPTION.

    Returns
    -------
    None.

    """

    drink_answer = input('Do you want to order a drink? [y]/n ')

    if drink_answer.lower() == 'n':
        print('See you in three songs!\n')

    else:

        nb_users = len(users)
        bottle_answer = input('Do you want a bottle ? [n]/y ')

        if bottle_answer.lower() == 'y':
            print('Here\'s the list of bottles we have :\n----------')

            for key, value in alcohol_bottle.items():
                print('{}: {} Tugrug'.format(key, value))

            order = True

            while order:
                try:
                    bottle_name = input('Write the name of the bottle (case sensitive): ')
                    price_bottle = alcohol_bottle[bottle_name]

                    split_price = int(round(price_bottle / nb_users))

                    for key in users.keys():
                        users[key] += split_price

                    order = False

                except KeyError:
                    print('Sorry, this bottle doesn\'t exist.\n')

        drink_answer = input('Do you want single drinks ? [y]/n ')

        if drink_answer != 'n':
            print('Here\'s the list of drinks we have :\n----------')

            for key, value in alcohol_unit.items():
                print('{}: {} Tugrug'.format(key, value))

            for key in users.keys():
                try:
                    drink_name = input(
                        'What do you want to drink, {} ? (enter for nothing, case sensitive):\n'.format(key))
                    price_drink = alcohol_unit[drink_name]
                    users[key] += price_drink

                except KeyError:
                    pass


def get_bill(users):
    """
    Get the bill for everyone in the room of the karaoke bar.

    Parameters
    ----------
    users : DICT
        DESCRIPTION.

    Returns
    -------
    total_bill : INT.

    """

    total_bill = 0

    print('\nThe bill of you evening\n-----------')

    for key, value in users.items():
        print('{}: {} Tugrug'.format(key, value))

        total_bill += value

    return total_bill


if __name__ == '__main__':
    waiting_list = []

    add_songs(waiting_list, 1)

    users = create_users()
    order_drinks(users)
