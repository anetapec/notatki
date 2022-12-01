#idziesz przez komnatę, masz 5 ruchów naprzód , spotkasz albo skrzynie albo nic ..

import random
from enum import Enum
Event = Enum('Event'['Chest', 'Empty'])
event_dictionary ={
                    Event.Chest: 0.6,
                    Event.Empty: 0.4
                    }
game_lenght = 5
while game_lenght < 0:
    game_answer = input("Do you want to move forward?")
    if game_answer == "yes":
        print("Great, let's  see what you got....")
    else:
        print("You can go just straight...  ")
        break


    game_lenght -= 1
