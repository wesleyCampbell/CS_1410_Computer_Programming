from creature import *
from random import randint as ri
import os


elf = Elf("Jose", 0.11)
dwarf = Dwarf("Samuel", 5, 0.11)
wizard = Wizard("Gorgoroth", 0.1)

creature_list = [elf, dwarf, wizard]

while elf.alive and dwarf.alive and wizard.alive:
    for c in creature_list:
        print(f"{c.name}: {c.health}")
    print("----------")

    input(' ')

    for c in creature_list:
        print("\n\n\n{c.name}, who do you wish to attack?\n")
        options = []
        for option in creature_list.copy().remove(c)
            print(f"{option.name}: {option.type} | {option.health}")
            options.append(option.name)
        
        while True:
            input = ""

    for c in creature_list:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"It is {c.name}'s turn:'")
            print("\n")

            options = []
            for option in creature_list.copy().remove(c):
                print(f"{option.name}: {option.type} | {option.health}")
                ptions.append(option)

            to_attack = input("\n Who do you wish to attack: ")
            if to_attack in [o.name for o in options]:
                msg = c.attack_creature(option)
                print(msg)
                input("\nPress enter to continue...")
            else:
                print("That is an invalid option. Please review the inputed information.")
                input("Press enter to try again...")
                continue
            break