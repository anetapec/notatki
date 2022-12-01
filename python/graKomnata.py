#gra w której masz 5 ruchów w jedną stronę poprzez KOMNATĘ.
#Za każdym razem masz szansę spotkać po drodzę skrzynkę lub NIC.
#Skrzynki mają różne kolory.
#Kolor skrzynki oznacza jak rzadka jest ta skrzynka.
#zielona - 75%
#pomarańczowa - 20%
#fioletowa - 4%
#złota (legendarna) - 1%
#Ustaw, że jest 40% szansy, że nie spotkasz niczego. 60%, że będzie skrzynka.
#Ustaw złoto jako to co może "wypaść" ze skrzynki:
#zielony - 1000,
#pomaranczowy - 4000,
#fioletowy - 9000,
#zlota - 16000

import random
from enum import Enum

def findAproximateVale(value,percentRange):
    lowerValue = value - (percentRange / 100) * value
    highestValue = value + (percentRange / 100) * value
    return random.randint(lowerValue, highestValue)
Event = Enum('Event', ['skrzynia', 'nic'])

eventDicionary = {Event.skrzynia: 0.6, Event.nic: 0.4}
eventList = tuple(eventDicionary.keys())
eventProbility = tuple(eventDicionary.values())

Colours = Enum('Colours', {
                        'Green': 'zielony',
                        'Orange': 'pomarańczowy',
                        'Purple': 'fioletowy',
                        'Gold': 'złoty'
                        }
           )
chestColourDictionary = {
                            Colours.Green: 0.75,
                            Colours.Orange: 0.2,
                            Colours.Purple: 0.04,
                            Colours.Gold: 0.1
                        }
chestColourList = tuple(chestColourDictionary.keys())
chestColourProbility = tuple(chestColourDictionary.values())
rewardForCheats = {
                    chestColourList[reward]: (reward + 1) * (reward + 1) * 1000
                    for reward in range(len(chestColourList))
                    }

goldAcqiuerd = 0
print("Witaj w mojej grze Komnata")
gameLenght = 5
while gameLenght > 0:
    gamerAnswer = input("Chcesz poruszyć się do przodu?")
    if (gamerAnswer == "yes"):
        print("Zobaczmy co otrzymałeś...")

        drawEvent = random.choices(eventList, eventProbility)[0]
        if drawEvent == Event.skrzynia :
            print("Wylosowałeś skrzynię")
            drawColour = random.choices(chestColourList, chestColourProbility)[0]
            print("koloru", drawColour.value)
            gameReward = findAproximateVale(rewardForCheats[drawColour], 10)
            goldAcqiuerd = goldAcqiuerd + gameReward


        elif drawEvent == Event.nic :
            print("Niestety nic nie wylosowałeś, próbuj dalej ")
    else:
        print("Możesz poruszać się tylko do przodu ...")
        continue
    gameLenght = gameLenght - 1

print("Gratulacje otrzymałeś", goldAcqiuerd)
