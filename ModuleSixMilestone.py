"""
Program Name: ModuleSixMilestone - IT140
Program Description: Moving between room for Project  2
Author Name: Lee Kitchen
Date Created: 11/28/22
Notes: Concept of moving between rooms for Project 2.

"""
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}


def main():
    starting_room = 'Great Hall'
    current_room = starting_room
    while True:
        print('You are in the', current_room + '.')
        move = input('Where would you like to go, North,East,South or West?(Quit to end): ').split()[-1].capitalize()
        if move == "Quit":
            break
        elif move in rooms[current_room]:
            current_room = rooms[current_room][move]
            print('Moving to {}'.format(current_room))
            continue
        else:
            print('Sorry that not a way you can go')
            print()
    print('Thanks for playing!')

main()