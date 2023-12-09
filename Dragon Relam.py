import random 
import time

def cave_message():
    print("\n"'''You are in a land full of dragons. In front of you,
you see __TWO__ caves. In one cave, the dragon is __FRIENDLY__
and will share his __TREASURE__ with you. The other dragon
is __GREEDY__ and hungry, and will __EAT__ you on sight.''' "\n")    #Multiline string ('''TEXT''')


def chose_cave():
    number = int(input('Which cave will you go into? (1 or 2)   '))
    time.sleep(2)                                                              #The time module has a function called sleep() that pauses the program.
    print('You approached the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(7)

    friendly_cave = random.randint(1,2)

    if friendly_cave == number:
        print('Gives you his treasure!')
    else:
       print('Gobbles you down in one bite!')


playthe_game = "yes"
while playthe_game == 'yes' or playthe_game == "y":
    cave_message()
    time.sleep(3)
    cave_number = chose_cave()
    print()
    time.sleep(2)
    playthe_game = input('Do you want to play again? (yes or no)  ')
