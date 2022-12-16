"""
Class: IT 140
Program Description: Texted Based Adventure Game for project 2
Author Name: Lee Kitchen
Date Created: 12/5/22
"""
import sys

def instructions():
    print('Welcome to the Adventure!')
    print('The evil Rictavio Perricules has captured your princess! Collect all 6 mystic items ')
    print('to defeat them and save the Princess! Be on the lookout for the secret tunnel,')
    print('and item there may aid you in your fight against Rictavio’s evil plot.')
    print('You can enter north,south,east or west to move.')
    print('If there is an item simple type it to get it.')
    print('Find all 6 items to enter the Boss room unharmed')
    print('********************')
# function
def get_new_state(state, direction):
        new_state = state
        for i in rooms:
            if i == state:  # if
                if direction in rooms[i]:
                    new_state = rooms[i][direction]

        return new_state  # return

rooms = {'Courtyard': {'East': 'Foyer'},
             'Foyer': {'West': 'Courtyard', 'North': 'Kitchen', 'East': 'Master Bedroom', 'South': 'Great Hall'},
             'Great Hall': {'North': 'Foyer', 'East': 'Library',},
             'Library': {'West': 'Great Hall'},
             'Kitchen': {'South': 'Foyer', 'East': 'Broom Closet'},
             'Broom Closet': {'North': 'Secret Tunnel', 'West': 'Kitchen'},
             'Secret Tunnel': {'South': 'Broom Closet'},
             'Master Bedroom': {'West': 'Foyer', 'North': 'Boss Room'},
             'Boss Room':'Ricktavio'
                 }
items = {'Courtyard':' ',
        'Foyer': 'Magic Sabatons',
        'Great Hall': 'Magic Sword',
        'Library': 'Magic Helm',
        'Kitchen': 'One UP',
        'Broom Closet':'Magic Gauntlets',
        'Secret Tunnel': 'Magic Gem',
        'Master Bedroom': 'Magic Chest plate',
        'Boss Room': 'Ricktavio'
    }
state = 'Courtyard'
inventory = []
instructions()

while 1:  #while statment for game loop
    print('You are in the ', state)
    if state == 'Boss Room':
        print('Battling with the villain', end='')#boss battle timer
        for i in range(50):
            for j in range(1000000):
                pass
            print(".", end='', flush=True)
        print()
        if len(inventory) == 6:
                print('You won - congratulations....')
                print('But unfortunately the Princess is in a different Castle')
        elif len(inventory) == 7:
                print('Congratulations --- You won!!! And you saved the princess')
        else:
                print('Sorry, you lost - be better armed next time')
        break
    print('*********************************')
    print('Available to you in this room is', items[state])
    print('You currently have', inventory)
    direction = input('Enter item you want OR direction to go OR exit to give up: ')
    print('*********************************')
    print()
    if direction.lower() == items[state].lower():
        if items[state] not in inventory:
                inventory.append(items[state])
        continue
    direction = direction.capitalize()
    if direction == 'Exit':
        sys.exit(0)
    if direction == 'East' or direction == 'West' or direction == 'North' or direction == 'South':
        new_state = get_new_state(state, direction)
        if new_state == state:
                print('There is a fearsome darkness in that direction, you quickly return to previous room!')
        else:
                state = new_state
    else:
            print('Invalid direction!!')