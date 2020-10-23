from creature import *
from random import randint as ri
import os


def print_creatures(creatures):
    for c in creatures:
        print(f"{c.name}: {c.type} | {c.health} health")
    print("--------------------")

elf = Elf("Jose", 0.11)
dwarf = Dwarf("Samuel", 5, 0.11)
wizard = Wizard("Gorgoroth", 0.1)

creature_list = [elf, dwarf, wizard]

while True:
    print_creatures(creature_list)

    input(' ')

    for c in creature_list:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        while True:
            print(f"It is {c.name}'s turn:'")
            print("\n")

            # Print out every other creature
            c_creature_list = creature_list.copy()
            c_creature_list.remove(c)
            print_creatures(c_creature_list)

            print("\n")

            choice = input("Who do you wish to attack: ")

            if choice in [i.name for i in c_creature_list]:
                for option in c_creature_list:
                    # If user chose this creature attack it
                    if option.name == choice:
                        msg = c.attack_creature(option)
                        print("\n" + msg)
                        input("\nPress enter to continue...")
                        break
                break
            # If input does not match any creature, try again
            else:
                print("That is an invalid choice. Please review the name.")
                input("\nPress enter to try again...")
            continue


